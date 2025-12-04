use flate2::write::GzEncoder;
use flate2::Compression;
use std::fs::{self, File};
use std::io::{self, BufRead, BufReader, BufWriter, Write};
use std::path::Path;
use std::time::Instant;

/// 配置：允许的标准库 Crate 列表 (白名单)
const ALLOWED_CRATES: &[&str] = &["std", "core", "alloc", "proc_macro", "test"];

/// 配置：必须切除的谓词 (黑名单)
const DENY_PREDICATES: &[&str] = &[
    "/prop/fullDoc>",        // 大段文档文本
    "/prop/hasExampleCode>", // 示例代码
    "/prop/doc_html>",       // HTML 格式文档
];

/// 路径配置 (相对于 Cargo.toml 所在的目录)
const INPUT_DIR: &str = "../../data/raw";
const OUTPUT_FILE: &str = "../data/dist/rust-std-1.89.0.nt.gz";

fn main() -> io::Result<()> {
    let start_time = Instant::now();
    println!("=== Rust Std Graph Slicer v1.1 (Strict Mode) ===");
    println!("Source: {}", INPUT_DIR);
    println!("Target: {}", OUTPUT_FILE);

    // 1. 准备输出流
    if let Some(parent) = Path::new(OUTPUT_FILE).parent() {
        fs::create_dir_all(parent)?;
    }
    let out_file = File::create(OUTPUT_FILE)?;
    let enc = GzEncoder::new(out_file, Compression::best());
    let mut writer = BufWriter::new(enc);

    let paths = fs::read_dir(INPUT_DIR)?;
    let mut grand_total_lines = 0;
    let mut grand_kept_lines = 0;

    // 2. 遍历处理每个文件
    for path in paths {
        let path = path?.path();
        // 只处理 .nt 文件
        if path.extension().and_then(|s| s.to_str()) == Some("nt") {
            let filename = path.file_name().unwrap().to_string_lossy();
            println!("\n--- Processing File: {} ---", filename);

            let file = File::open(&path)?;
            let reader = BufReader::new(file);

            let mut file_lines = 0;
            let mut file_kept = 0;
            let mut dropped_doc = 0;
            let mut dropped_crate = 0;

            for line in reader.lines() {
                let line = line?;
                file_lines += 1;

                if should_keep(&line, &mut dropped_doc, &mut dropped_crate) {
                    writeln!(writer, "{}", line)?;
                    file_kept += 1;
                }
            }

            println!("   Total: {}", file_lines);
            println!("   Kept:  {}", file_kept);
            println!("   Dropped (Docs):   {}", dropped_doc);
            println!("   Dropped (Alien):  {} (Non-std namespace)", dropped_crate);

            // 严谨性检查：如果在 Skeleton/Bridge 里发现了 Alien，我们要警惕
            if filename.contains("skeleton") || filename.contains("bridge") {
                if dropped_crate > 0 {
                    println!(
                        "   [WARNING] Found {} non-std items in structural file!",
                        dropped_crate
                    );
                } else {
                    println!("   [PASS] Structural integrity verified.");
                }
            }

            grand_total_lines += file_lines;
            grand_kept_lines += file_kept;
        }
    }

    println!("\n=== All Done ===");
    println!("Time: {:.2?}", start_time.elapsed());
    println!("Grand Total Lines: {}", grand_total_lines);
    println!("Grand Kept Lines:  {} (Saved to .gz)", grand_kept_lines);

    Ok(())
}

fn should_keep(line: &str, drop_doc_counter: &mut usize, drop_crate_counter: &mut usize) -> bool {
    // 1. 谓词黑名单检查
    for deny in DENY_PREDICATES {
        if line.contains(deny) {
            *drop_doc_counter += 1;
            return false;
        }
    }

    // 2. 命名空间检查 (Subject Crate Check)
    // 逻辑：提取 "/item/" 和之后的第一个 "." 之间的内容
    if let Some(start_idx) = line.find("/item/") {
        let content_after = &line[start_idx + 6..];
        if let Some(end_idx) = content_after.find('.') {
            let crate_name = &content_after[..end_idx];

            if !ALLOWED_CRATES.contains(&crate_name) {
                *drop_crate_counter += 1;
                return false;
            }
        }
    }
    // 注意：如果找不到 /item/ 格式（比如匿名节点 _:genid），默认保留
    // 这可能是一个潜在的宽松点，但在 N-Triples 中通常是安全的

    true
}

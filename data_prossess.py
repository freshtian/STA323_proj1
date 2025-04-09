import os
import gzip
# 配置路径
base_dir = "security-datasets01/maccdc-2012"
sub_dirs = ["00", "01", "02", "03", "04", "05"]
output_files = {
    "http": "http_merged.txt",
    "dns": "dns_merged.txt"
}
def merge_logs():
    # 初始化合并文件（清空已存在内容）
    for key in output_files:
        open(output_files[key], 'w').close()
    # 遍历所有子目录
    for sub_dir in sub_dirs:
        dir_path = os.path.join(base_dir, sub_dir)
        # 处理HTTP日志
        http_gz = os.path.join(dir_path, "http.log.gz")
        if os.path.exists(http_gz):
            with gzip.open(http_gz, 'rt') as f_in:
                content = f_in.read()
                with open(output_files["http"], 'a', encoding='utf-8') as f_out:
                    f_out.write(content + "\n")  # 添加换行分隔不同文件内容
        # 处理DNS日志
        dns_gz = os.path.join(dir_path, "dns.log.gz")
        if os.path.exists(dns_gz):
            with gzip.open(dns_gz, 'rt') as f_in:
                content = f_in.read()
                with open(output_files["dns"], 'a', encoding='utf-8') as f_out:
                    f_out.write(content + "\n")


if __name__ == "__main__":
    merge_logs()
    print(f"合并完成！生成文件：{list(output_files.values())}")

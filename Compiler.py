import subprocess
import os
import shutil

def compile_latex_batch(batch_dir: str = "./batch", output_dir: str = "./output", old_dir: str = "./old"):
    """Compiles all LaTeX files in the batch folder and moves them to the old folder after compilation."""
    if not os.path.exists(batch_dir):
        print(f"Batch folder '{batch_dir}' does not exist.")
        return

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    if not os.path.exists(old_dir):
        print(f"Old folder '{old_dir}' does not exist.")
        return

    tex_files = [f for f in os.listdir(batch_dir) if f.endswith(".tex")]

    if not tex_files:
        print("No .tex files found in the batch folder.")
        return

    for tex_file in tex_files:
        full_path = os.path.join(batch_dir, tex_file)
        output_pdf = os.path.join(output_dir, os.path.splitext(tex_file)[0] + ".pdf")

        try:
            subprocess.run(
                ["pdflatex", "-output-directory", output_dir, full_path],
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            print(f"Compiled: {output_pdf}")

            # Move .tex file to the old folder
            shutil.move(full_path, os.path.join(old_dir, tex_file))
            print(f"Moved {tex_file} to {old_dir}")

        except subprocess.CalledProcessError as e:
            print(f"Error compiling {tex_file}: {e.stderr.decode()}")

if __name__ == "__main__":
    compile_latex_batch()
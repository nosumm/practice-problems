import os
from pathlib import Path

def create_problem_structure(problem_name, problem_source="leetcode", difficulty="easy"):
    """
    Generates the folder structure for a new problem in Python, Java, and C.
    Checks for existing directories and files to avoid overwriting.
    """
    # Get current working directory (should be practice-problems)
    base_dir = Path.cwd()
    
    # Validate we're in practice-problems
    if base_dir.name != "practice-problems":
        print("Error: This script should be run from within the practice-problems directory")
        return False

    problem_dir = base_dir / problem_source / difficulty / problem_name
    
    # Check if problem already exists
    if problem_dir.exists():
        print(f"Problem already exists at: {problem_dir}")
        return False
    
    # Create parent directories if they don't exist
    (base_dir / problem_source).mkdir(exist_ok=True)
    (base_dir / problem_source / difficulty).mkdir(exist_ok=True)

    # Create language directories
    languages = ["python", "java", "c", "c++"]
    created_files = []
    
    for lang in languages:
        lang_dir = problem_dir / lang
        lang_dir.mkdir(parents=True, exist_ok=True)
        
        # Determine file paths
        if lang == "python":
            file_path = lang_dir / f"{problem_name}.py"
            content = f"""# Solution for {problem_name} (Python)
# Problem: https://{problem_source}.com/problems/{problem_name.replace('_', '-')}/
def solve():
    pass

if __name__ == '__main__':
    solve()"""
        elif lang == "java":
            class_name = problem_name.title().replace("_", "")
            file_path = lang_dir / f"{class_name}.java"
            content = f"""// Solution for {problem_name} (Java)
// Problem: https://{problem_source}.com/problems/{problem_name.replace('_', '-')}/
public class {class_name} {{
    public static void main(String[] args) {{
        System.out.println("Solution for {problem_name}");
    }}
}}"""
        elif lang == "c":
            file_path = lang_dir / f"{problem_name}.c"
            content = f"""// Solution for {problem_name} (C)
// Problem: https://{problem_source}.com/problems/{problem_name.replace('_', '-')}/
#include <stdio.h>

int main() {{
    printf("Solution for {problem_name}\\n");
    return 0;
}}"""
        elif lang == "c++":
            file_path = lang_dir / f"{problem_name}.cpp"
            content = f"""// Solution for {problem_name} (C++)
// Problem: https://{problem_source}.com/problems/{problem_name.replace('_', '-')}/
#include <stdio.h>

int main() {{
    printf("Solution for {problem_name}\\n");
    return 0;
}}"""

        # Only create file if it doesn't exist
        if not file_path.exists():
            file_path.write_text(content)
            created_files.append(file_path)
        else:
            print(f"File already exists: {file_path}")

    # Create README only if problem directory is new
    readme_path = problem_dir / "README.md"
    if not readme_path.exists():
        readme_content = f"""# {problem_name.replace('_', ' ').title()}

## Problem
Source: [{problem_source}](https://{problem_source}.com/problems/{problem_name.replace('_', '-')}/)

## Solutions
| Language | File |
|----------|------|
| Python | [{problem_name}.py](python/{problem_name}.py) |
| Java | [{problem_name.title().replace('_', '')}.java](java/{problem_name.title().replace('_', '')}.java) |
| C | [{problem_name}.c](c/{problem_name}.c) |"""
        readme_path.write_text(readme_content)
        created_files.append(readme_path)
    else:
        print(f"README already exists: {readme_path}")

    if created_files:
        print(f"\nCreated problem structure at: {problem_dir}")
        print("New files created:")
        for file in created_files:
            print(f"- {file}")
    else:
        print("No new files created (all files already existed)")

    return True

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Generate a new problem folder structure.")
    parser.add_argument("problem_name", help="Name of the problem (e.g., 'two_sum')")
    parser.add_argument("--source", default="leetcode", help="Problem source (e.g., 'leetcode', 'hackerrank')")
    parser.add_argument("--difficulty", default="easy", help="Difficulty level (e.g., 'easy', 'medium', 'hard')")
    args = parser.parse_args()
    
    create_problem_structure(args.problem_name, args.source, args.difficulty)

# -*- coding: UTF-8 -*-
from jinja2 import Template
import json


def generate_config(template_file, data_file, output_file):
    try:
        """
        使用Jinja2模板和JSON数据生成配置文件
    
        参数:
        - template_file: 模板文件的路径 (str)
        - data_file: 包含变量值的JSON文件路径 (str)
        - output_file: 输出配置文件的路径 (str)
        """

        # 加载JSON数据
        with open(data_file, 'r') as file_data:
            data = json.load(file_data)

        # 加载模板文件
        with open(template_file, 'r') as file_template:
            template_content = file_template.read()
        template = Template(template_content)

        # 渲染模板并生成配置内容
        rendered_content = template.render(data)

        # 将渲染后的内容写入到输出文件
        with open(output_file, 'w') as file_output:
            file_output.write(rendered_content)
    except IOError as e:
        print(f"IOError: {e}")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 4:
        print("Usage: python render_template.py <template_file> <data_file> <output_file>")
    else:
        template_file, data_file, output_file = sys.argv[1:]
        generate_config(template_file, data_file, output_file)

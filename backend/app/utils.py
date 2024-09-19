# utils.py

import os
import yaml
import zipfile
import datetime
import psycopg2
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image

class ProjectManager:
    def __init__(self, project_name):
        self.project_name = project_name
        self.files = [
            "app.js",
            "pages/index/index.js",
            "pages/index/index.wxml",
            "pages/index/index.wxss",
            "project.config.json",
            "LICENSE",
            "sitemap.json"
        ]

    def create_project_structure(self):
        os.makedirs(f"{self.project_name}/pages/index", exist_ok=True)

        for file_path in self.files:
            full_path = os.path.join(self.project_name, file_path)
            with open(full_path, "w") as file:
                file.write("")  # 创建空文件

        with zipfile.ZipFile(f"{self.project_name}.zip", 'w') as zipf:
            for root, _, files in os.walk(self.project_name):
                for file in files:
                    zipf.write(os.path.join(root, file))

        print(f"项目文件已创建并压缩为 {self.project_name}.zip")

class Logger:
    def __init__(self, project_name):
        self.log_file = os.path.join(project_name, "temp/OneDC_Updater", 'update.log')

    def log_message(self, message):
        os.makedirs(os.path.dirname(self.log_file), exist_ok=True)
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open(self.log_file, 'a') as file:
            file.write(f"{timestamp} - {message}\n")

    def perform_update(self):
        self.log_message("Update started")
        
        try:
            # 模拟下载新数据
            self.log_message("Downloaded new data")
            
            # 模拟处理数据
            self.log_message("Data processed")
            
            self.log_message("Update completed successfully")
        except Exception as e:
            self.log_message(f"Update failed: {str(e)}")

class ConfigLoader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.config = self.load_config()

    def load_config(self):
        """
        Load configuration from a YAML file.
        """
        with open(self.file_path, 'r') as file:
            config = yaml.safe_load(file)
        return config

    def get_api_key(self, service_name):
        """
        Retrieve the API key for a given service.
        """
        return self.config['api_keys'].get(service_name)

class DatabaseConnector:
    def __init__(self, config):
        self.config = config
        self.connection = self.connect_to_database()

    def connect_to_database(self):
        """
        Connect to the database using the configuration provided.
        """
        conn = psycopg2.connect(
            host=self.config['database']['host'],
            port=self.config['database']['port'],
            user=self.config['database']['user'],
            password=self.config['database']['password'],
            dbname=self.config['database']['name']
        )
        return conn

class DiagramGenerator:
    def __init__(self, output_path):
        self.output_path = output_path

    def generate_system_design_diagram(self):
        fig, ax = plt.subplots(figsize=(12, 8))

        # Frontend components
        frontend_components = [
            {"name": "Homepage", "x": 0.1, "y": 0.8},
            {"name": "Organization", "x": 0.1, "y": 0.5},
            {"name": "My Profile", "x": 0.1, "y": 0.2}
        ]

        # Backend components
        backend_components = [
            {"name": "API Layer", "x": 0.6, "y": 0.7},
            {"name": "Authentication", "x": 0.6, "y": 0.5},
            {"name": "Database", "x": 0.6, "y": 0.3}
        ]

        # Add frontend boxes and labels
        for component in frontend_components:
            ax.add_patch(patches.Rectangle((component["x"], component["y"]), 0.3, 0.1, edgecolor='black', facecolor='lightblue'))
            ax.text(component["x"] + 0.15, component["y"] + 0.05, component["name"], horizontalalignment='center', verticalalignment='center')

        # Add backend boxes and labels
        for component in backend_components:
            ax.add_patch(patches.Rectangle((component["x"], component["y"]), 0.3, 0.1, edgecolor='black', facecolor='lightgreen'))
            ax.text(component["x"] + 0.15, component["y"] + 0.05, component["name"], horizontalalignment='center', verticalalignment='center')

        # Draw arrows between frontend and backend components
        for frontend in frontend_components:
            ax.annotate("", xy=(0.4, frontend["y"] + 0.05), xytext=(0.6, 0.75), arrowprops=dict(arrowstyle="->"))
            ax.annotate("", xy=(0.4, frontend["y"] + 0.05), xytext=(0.6, 0.55), arrowprops=dict(arrowstyle="->"))
            ax.annotate("", xy=(0.4, frontend["y"] + 0.05), xytext=(0.6, 0.35), arrowprops=dict(arrowstyle="->"))

        # Draw arrows between API layer and other backend components
        ax.annotate("", xy=(0.75, 0.75), xytext=(0.75, 0.85), arrowprops=dict(arrowstyle="->"))
        ax.annotate("", xy=(0.75, 0.55), xytext=(0.75, 0.65), arrowprops=dict(arrowstyle="->"))
        ax.annotate("", xy=(0.75, 0.35), xytext=(0.75, 0.45), arrowprops=dict(arrowstyle="->"))

        # Add WeChat Mini Program API box
        ax.add_patch(patches.Rectangle((0.6, 0.1), 0.3, 0.1, edgecolor='black', facecolor='lightcoral'))
        ax.text(0.75, 0.15, "WeChat Mini Program API", horizontalalignment='center', verticalalignment='center')

        # Add arrows from frontend to WeChat Mini Program API
        for frontend in frontend_components:
            ax.annotate("", xy=(0.4, frontend["y"] + 0.05), xytext=(0.6, 0.15), arrowprops=dict(arrowstyle="->"))

        # Set the title and remove axes
        ax.set_title("System Design Diagram for Web Application")
        ax.axis('off')

        # Save the figure
        plt.savefig(self.output_path)
        print(f"System Design Diagram saved as {self.output_path}")

class ImageConverter:
    def __init__(self, webp_dir, output_dir):
        self.webp_dir = webp_dir
        self.output_dir = output_dir

    def convert_webp_to_png(self):
        os.makedirs(self.output_dir, exist_ok=True)

        for filename in os.listdir(self.webp_dir):
            if filename.endswith(".webp"):
                webp_path = os.path.join(self.webp_dir, filename)
                img = Image.open(webp_path)
                
                # 修改扩展名并保存
                output_path = os.path.join(self.output_dir, os.path.splitext(filename)[0] + ".png")
                img.save(output_path, "PNG")
        print(f"All WebP images converted and saved to {self.output_dir}")

if __name__ == "__main__":
    # 项目管理
    project_manager = ProjectManager("mini_program_project")
    project_manager.create_project_structure()
    
    # 日志记录与更新
    logger = Logger("mini_program_project")
    logger.perform_update()

    """
    # 配置加载
    config_loader = ConfigLoader('config.yaml')
    db_connection = DatabaseConnector(config_loader.config)
    api_key = config_loader.get_api_key('service_1')
    print(f"API Key for service_1: {api_key}")

    # 生成系统设计交互图
    diagram_generator = DiagramGenerator("/mnt/data/English_System_Design_Diagram.png")
    diagram_generator.generate_system_design_diagram()
    """

    # 转换 WebP 图片为 PNG
    image_converter = ImageConverter("../database", "../database/png")
    image_converter.convert_webp_to_png()

# utils/logger_utils.py
import logging
import os
import time


def get_logger(name="api_auto_test"):
    # 1. 创建日志器
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)  # 设置最低级别为 DEBUG

    # 防止重复添加 Handler（多次调用时日志会重复打印）
    if logger.handlers:
        return logger

    # 2. 创建日志格式
    # 格式：时间 - 级别 - 文件名[行号] - 消息
    formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(filename)s[line:%(lineno)d] - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # 3. 控制台输出 (StreamHandler)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)  # 控制台只打印 INFO 及以上级别
    console_handler.setFormatter(formatter)

    # 4. 文件输出 (FileHandler)
    # 确保 logs 文件夹存在
    log_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # 文件名带上日期，比如 api_test_2023-10-25.log
    log_file = os.path.join(log_dir, f"api_test_{time.strftime('%Y-%m-%d')}.log")
    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)  # 文件里记录最详细的 DEBUG 级别
    file_handler.setFormatter(formatter)

    # 5. 把 Handler 添加到 Logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger


# 实例化一个全局日志对象，方便其他文件直接 import
logger = get_logger()

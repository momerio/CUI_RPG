# はじめに実行するやつ

# ライブラリ
import logging
import datetime
# ユーザ定義
import InitialScene

## ログ設定 ##
now_time = datetime.datetime.now().strftime('%Y_%m_%d_%H-%M-%S')
log_directory_path = "log/"
formatter = "【%(asctime)s】%(levelname)s : %(message)s"
logger = logging.getLogger(__name__)
logging_handler = logging.FileHandler(filename=log_directory_path + now_time +
                                      ".log", encoding="utf-8")
logging_handler.setLevel(logging.DEBUG)
logger.setLevel(logging.DEBUG)
logging_handler.setFormatter(logging.Formatter(formatter))
logger.addHandler(logging_handler)

logger.info('runを実行')

ret = InitialScene.run()

if ret == 0:  # 正常終了
    logger.info("Info: 正常終了!(run,)")
else:
    logger.info(f"Erro: 異常終了 ret={ret} (run,)")

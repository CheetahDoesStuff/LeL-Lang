from usefullog import logger
from platformdirs import user_log_dir
from pathlib import Path
from sys import exit as sys_exit

log_dir = Path(user_log_dir("LeLlang"))
log_dir.mkdir(parents=True, exist_ok=True)



log = logger.Logger(
    "LeLlang",
    do_timestamps=False,
    do_log_saving=True,
    log_save_folder=str(log_dir)
)

file_path: str = ""
output_path: str = ""



def exit(msg: str = "Exiting the program..."):
    if msg:
        log.critical(msg)

    sys_exit(1)
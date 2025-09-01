from usefullog import logger
from platformdirs import user_log_dir

log = logger.Logger(
    "LeLlang",
    do_timestamps=False,
    do_log_saving=True,
    log_save_folder=user_log_dir("LeLlang")
)

file_path: str = ""

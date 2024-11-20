import os
import shutil
import zipfile
from pathlib import Path

from src.problem import Problem

PATH_TMP_FOLDER = Path("temp")


class Generator(Problem):
    def __init__(self, pid: str):
        super().__init__(pid)

    @staticmethod
    def __ensure_and_clear_temp_folder():
        if not PATH_TMP_FOLDER.exists():
            PATH_TMP_FOLDER.mkdir(parents=True)
        for file in PATH_TMP_FOLDER.iterdir():
            os.remove(file)

    @staticmethod
    def __compile(path: Path):
        if os.system(f"g++ {path} -o {PATH_TMP_FOLDER / path.stem} -O2 -std=c++20 -Wl,--stack=268435456"):
            raise Exception(f"{path} 编译失败")

    def generate(self):
        self._logger.info("生成测试数据")

        self._logger.debug("清空临时文件夹")
        self.__ensure_and_clear_temp_folder()
        if not self._path_std.exists():
            raise Exception("标程不存在")

        self._logger.info("编译标程")
        self.__compile(self._path_std)

        self._logger.info("生成输入样例")
        if self._path_gen_cpp.exists():
            self._logger.info("编译生成器")
            self.__compile(self._path_gen_cpp)
            os.system(f"cd {PATH_TMP_FOLDER} && gen")
        elif self._path_gen_py.exists():
            shutil.copy(self._path_gen_py, PATH_TMP_FOLDER)
            os.system(f"cd {PATH_TMP_FOLDER} && python gen.py")
        else:
            raise Exception("生成器不存在")

        self._logger.info("生成输出样例")
        files_input = PATH_TMP_FOLDER.glob("*.in")
        for file in files_input:
            os.system(f"{PATH_TMP_FOLDER / 'std'} < {file} > {PATH_TMP_FOLDER / (file.stem + '.out')}")
            self._logger.info(f"输出样例 #{file.stem} 已生成")

        self._logger.info("打包测试数据")
        path_zip = self._path / "testcase.zip"
        path_zip.unlink(missing_ok=True)
        with zipfile.ZipFile(path_zip, "w") as zip_file:
            for file in PATH_TMP_FOLDER.iterdir():
                if file.suffix in [".in", ".out"]:
                    zip_file.write(file, file.name)

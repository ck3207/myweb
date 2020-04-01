import os
import time
import zipfile
import logging

class Replace:
    """替换配置文件"""
    def __init__(self, file_path, section):
        """file_path is the path of the zipfile."""
        self.file_path = file_path
        self.section = section
        
    def unzip_file(self):
        """
        Extract zip file!
        Argue path is the absolutely dir of the target zipfile.
        Argue file is the one which will be extract!
        """
        try:
            file_name = os.path.basename(self.file_path)
            file_path = os.path.dirname(self.file_path)
            logging.info('The zip file_path is [{0}], file_name is [{1}]'.format(file_path, file_name))
            if not zipfile.is_zipfile(self.file_path):
                self.file_path = os.path.join(file_path, self.rename_filename(filename=file_name))
                logging.info("The zip file can not recoganized to be a  zipfile.")
            if not os.path.exists(self.file_path):
                logging.info("The zip file_full_path cant be found.")
                raise FileNotFoundError("File do not exist:　", self.file_path)
            zip_package = zipfile.ZipFile(file=self.file_path, mode="r") # 被解压的文件对象

            
            # 指定解压目录，并清理该目录
            extract_dir = os.path.join(os.path.dirname(self.file_path), file_name[:-4])
            self.__clean_env(extract_dir)
            if not os.path.exists(extract_dir):
                os.mkdir(extract_dir) # 创建zip文件解压后的存放路径
                logging.debug('create directory [{0}]'.format(extract_dir))
            zip_package.extractall(extract_dir) #解压文件到指定路径
            logging.info("Unzip file[%s] Successfully!" % file_name)
            file_name = file_name[:-4]+"-replaced.zip"  # 压缩文件名
            # src_dir = self.get_next_dir(extract_dir)    # 需压缩的文件目录
            src_dir = extract_dir    # 需压缩的文件目录 (此目录的文件会被压缩)
            target_dir = file_path # 压缩到哪个目录

            if not os.path.exists(target_dir):
                os.mkdir(target_dir)
                logging.debug('create directory [{0}]'.format(target_dir))
            # logging.info(src_dir, target_dir, file_name)
            return src_dir, target_dir, file_name
        except Exception as e:
            logging.info("Unzip file[%s] failed!" % file_name)
            logging.info("Error:{0}".format(str(e)))
        finally:
            zip_package.close()

    def zip_file(self, src_dir, dest_dir, file_name):
        """Argue src_dir is the dir that will be compressed.
        Argue dest_dir is the dir for saving.
        Argue file_name is the zipfile name."""
        compress_zip_file = zipfile.ZipFile(os.path.join(dest_dir, file_name), mode="w", compression=zipfile.ZIP_DEFLATED)
        try:
            replaced_path = src_dir + os.sep # 被压缩文件的目录
            logging.info("TargetDir: {}".format(replaced_path))
            current_path = os.getcwd()
            os.chdir(replaced_path)
            for dirpath, dirnames, filenames in os.walk(src_dir):
                for filename in filenames:
                    # 需替换路径前缀，否则会完全把路径也写入到压缩文件内
                    compress_zip_file.write(os.path.join(dirpath, filename).replace(replaced_path, ''))
            logging.info("Compress To Zipfile Successfully!")
            os.chdir(current_path)
            return os.path.join(dest_dir, file_name)
        except Exception as e:
            logging.info("Compress Files[{0}] Error:{1}".format(src_dir, str(e)))
        finally:
            os.chdir(current_path)
            compress_zip_file.close()

    def get_next_dir(self, src):
        """Get the next dir in the src."""
        for each in os.listdir(src):
            if os.path.isdir(os.path.join(src, each)):
                return os.path.join(src, each)

    def __clean_env(self, path="download"):
        if not os.path.exists(path):
            return
        if os.name == "nt":
            rm_command = "rd /s /q " + path
        elif os.name == "posix":
            rm_command = "rm -rf " + path
        logging.info("Clean Command: {0}".format(rm_command))
        os.popen(rm_command)
        time.sleep(1)

    def replace_config(self, right_config_path, replaced_config_path, config_name="config.js"):
        """
        Argue right_config_path is the right config in which thr config file will be used.
        Argue replaced_config is the wrong config directory in which the config file will be replaced.
        """
        right_config = os.path.join(right_config_path, config_name)
        replace_config = os.path.join(replaced_config_path, config_name)
        logging.info("Right Config: ",right_config, "\nReplaced Config:", replace_config)
        if not (os.path.exists(right_config) and os.path.exists(replace_config)):
            logging.info("File Not Exists [{0}], [{1}]".format(right_config, replace_config))
        if os.name == "nt":
            command = "copy /Y {0} {1}".format(right_config.replace('/', '\\'), replace_config.replace('/', '\\'))
        elif os.name == "posix":
            command = "yes | cp {0} {1}".format(right_config, replaced_config)
        logging.info("Replace config.js command: {0}".format(command))
        os.popen(command)
        time.sleep(0.5)
        
    def rename_filename(self, filename):
        """If file is not a zipfile when tested in func zipfile.is_zipfile(filename=file),
        then replace the filename .
        """
        return filename.replace(".", "-") 
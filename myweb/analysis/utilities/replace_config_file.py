import os
import time
import logging

import zipfile


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
            logging.info('Into Replace.unzip_file...')
            if os.path.exists(self.file_path):
                file_path = os.path.dirname(self.file_path)
                file_name = os.path.basename(self.file_path)
                # os.chdir(os.path.dirname(self.file_path))
            if not zipfile.is_zipfile(self.file_path):
                logging.error('The zipfile[{0}] cant be recoginized.'.format(file_name))
            logging.info('The zipfile[{0}] can be recoginized as a zipfile.'.format(self.file_path))
            zip_package = zipfile.ZipFile(file=self.file_path) # 被解压的文件对象

            # 指定解压目录，并清理该目录
            extract_dir = os.path.join(file_path, file_name[:-4])
            self.clean_env(extract_dir)
            if not os.path.exists(extract_dir):
                os.mkdir(extract_dir) #创建zip文件解压后的存放路径
            
            zip_package.extractall(extract_dir) #解压文件到指定路径
            logging.info("Unzip file[%s] Successfully!" % file_name)
            new_file_name = extract_dir+"-replaced.zip"  # 压缩文件名
            src_dir = extract_dir    # 需压缩的文件目录
            target_dir = file_path # 压缩到哪个目录

            # if not os.path.exists(target_dir):
                # os.mkdir(target_dir)
            return (src_dir, target_dir, new_file_name)
        except Exception as e:
            logging.info("Unzip file[%s] failed!" % file_name)
            logging.info("Error:{0}".format(str(e)))
        finally:
            zip_package.close()


    def zip_file(self, src_dir, dest_dir, file_name):
        """Argue src_dir is the dir that will be compressed.
        Argue dest_dir is the dir for saving.
        Argue file_name is the zipfile name."""
        compress_zip_file = zipfile.ZipFile(os.path.join(dest_dir, file_name), "a", zipfile.ZIP_DEFLATED)
        try:
            replaced_path = src_dir + os.sep
            current_path = os.getcwd()
            os.chdir(replaced_path)

            for dirpath, dirnames, filenames in os.walk(src_dir):
                for filename in filenames:
                    relative_path = os.path.join(dirpath, filename).replace(replaced_path, "")
                    compress_zip_file.write(relative_path)
            logging.info("Compress To Zipfile Successfully!")
            os.chdir(current_path)
            return os.path.join(dest_dir, file_name)
        except Exception as e:
            logging.info("Compress Files[{0}] Error:{1}".format(src_dir, str(e)))
        finally:
            compress_zip_file.close()


    def get_next_dir(self, src):
        """Get the next dir in the src."""
        for each in os.listdir(src):
            if os.path.isdir(os.path.join(src, each)):
                return os.path.join(src, each)


    def clean_env(self, path="download"):
        if not os.path.exists(path):
            return
        if os.name == "nt":
            rm_command = "rd /s /q " + path
        elif os.name == "posix":
            rm_command = "rm -rf " + path
        logging.info("Clean Command: {0}".format(rm_command))
        os.popen(rm_command)
        time.sleep(1)


    def replace_config(self, origin_config_path, be_replaced_path, filename):
        origin_config = os.path.join(origin_config_path, filename)
        be_replaced = os.path.join(origin_config_path, filename)
        if os.name == "nt":
            command = "copy /Y {0} {1}".format(origin_config, be_replaced)
        elif os.name == "posix":
            command = "yes | cp {0} {1}".format(origin_config, be_replaced)
        logging.info("Replace {0} command: {1}".format(filename, command))
        os.popen(command)
        time.sleep(0.5)
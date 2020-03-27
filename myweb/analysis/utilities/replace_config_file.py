


class Replace:
    """替换配置文件"""
    def __init__(self, file_path):
        """file_path is the path of the zipfile."""
        self.file_path = file_path
        
    def unzip_file(self):
    """Extract zip file!
    Argue path is the absolutely dir of the target zipfile.
    Argue file is the one which will be extract!"""
    try:
        if os.path.exists(self.file_path):
            os.chdir(os.path.dirname(self.file_path))
        zip_package = zipfile.ZipFile(os.path.basename(self.file_path)) # 被解压的文件对象

        # 指定解压目录，并清理该目录
        extract_dir = file[:-4]

        os.mkdir(extract_dir) #创建zip文件解压后的存放路径
        zip_package.extractall(extract_dir) #解压文件到指定路径
        print("Unzip file[%s] Successfully!" % file)
        file_name = extract_dir+".zip"  # 压缩文件名
        src_dir = _get_next_dir(os.path.join(path, extract_dir))    # 需压缩的文件目录
        target_dir = os.path.join(path, "packages") # 压缩到哪个目录

        if not os.path.exists(target_dir):
            os.mkdir(target_dir)
        return _zip(src_dir=src_dir, dest_dir=target_dir, file_name=file_name)
    except Exception as e:
        print("Unzip file[%s] failed!" % file)
        print("Error:", str(e))
    finally:
        zip_package.close()


    def zip_file(self, src_dir, dest_dir, file_name):
        """Argue src_dir is the dir that will be compressed.
        Argue dest_dir is the dir for saving.
        Argue file_name is the zipfile name."""
        compress_zip_file = zipfile.ZipFile(os.path.join(dest_dir, file_name), "a", zipfile.ZIP_DEFLATED)
        try:
            replaced_path = src_dir + os.sep
            os.chdir(replaced_path)

            for dirpath, dirnames, filenames in os.walk(src_dir):
                for filename in filenames:
                    relative_path = os.path.join(dirpath, filename).replace(replaced_path, "")
                    compress_zip_file.write(relative_path)
            print("Compress To Zipfile Successfully!")
            return os.path.join(dest_dir, file_name)
        except Exception as e:
            print("Compress Files[%s] Error:%s", (src_dir, str(e)))
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
        print("Clean Command: ", rm_command)
        os.popen(rm_command)
        time.sleep(1)


    def replace_config(self, origin_config, be_replaced):
        if os.name == "nt":
            command = "copy /Y {0} {1}".format(origin_config, be_replaced)
        elif os.name == "posix":
            command = "yes | cp {0} {1}".format(origin_config, be_replaced)
        print("Replace config.js command: ", command)
        os.popen(command)
        time.sleep(0.5)
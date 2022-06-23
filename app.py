import typing


class FileHandler:
    """
        A class to find and replace the contnet in a file.

        ...

        Attributes
        ----------
        file_path : str
            path of the file to read and replace
        
        Methods
        -------
        __read_file() -> str:
            Reads the file and returns with the content
        
        """

    def __init__(self, file_path) -> None:
        self.file_path = file_path

    def __read_file(self) -> str:
        with open(self.file_path, 'r') as f:
            return f.read()

    def __write_file(self, contents: str) -> None:
        with open(self.file_path, 'w') as f:
            f.write(contents)
            
    
    def find_and_replace(self,source:str, target:str) -> typing.Tuple[bool, str]:
        """
            Find and replace string.

            This function simple replace the source string with target. 
            
            Parameters
            ----------
            source : str
                Source string to be replaced with
            target : str
                Target string 

            Returns
            -------
            tuple(bool,str)
                bool : status of the operation True / False
                    True : If there is not error in the operation 
                    False : If any error / exception happend in the operation

            str : sucess message or exception message based on the bool value
            
        """

        isSuccess = True
        msg = "successfully completed"

        try:
            source_content = self.__read_file()
            target_content = source_content.replace(source, target)
            self.__write_file(contents=target_content)
        except Exception as ex:
            msg = str(ex)
            isSuccess = False
         
        return (isSuccess, msg)
  

if __name__ == "__main__":
    f_handler = FileHandler("example.txt")
    status,msg = f_handler.find_and_replace("placement", "screening")
    print(f"status : {status}")
    print(f"msg : {msg}")
    
     
 
 
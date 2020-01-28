import PyPDF2
import os
import shutil
import secrets
import string


class SetPasswords:

    def __init__(self, input_dir, mother_pass, password_length):
        self.input_dir = input_dir
        self.mother_pass = mother_pass
        self.password_length = password_length

    @staticmethod
    def create_password(length):
        # Create a password
        return "".join(secrets.choice(string.printable.strip()) for _ in range(length))

    def set_password(self, input_file):
        # This is the main function, that sets a password to a single file

        path, filename = os.path.split(input_file)

        # Read file
        input_ = PyPDF2.PdfFileReader(open(os.path.join(self.input_dir, input_file), "rb"))

        # Skip if already encrypted
        if input_.isEncrypted:
            print(f"File {filename} is already encrypted, skipping it")
            return f"{filename} -------> Already encrypted"

        # Write output
        output_ = PyPDF2.PdfFileWriter()
        for page in input_.pages:
            output_.addPage(page)

        # Create output file
        output_file = os.path.join(path, f"temp_{filename}")
        output_stream = open(output_file, "wb")

        # Create and set password
        user_pass = self.create_password(self.password_length)
        output_.encrypt(user_pass, self.mother_pass, use_128bit=True)

        # Close stuff
        output_.write(output_stream)
        output_stream.close()

        # Swap old and new
        shutil.move(output_file, os.path.join(self.input_dir, input_file))

        # Return password to be stored
        return f"{filename} ------> {user_pass} \n"

    def set_multiple_passwords(self):
        # Set passwords to all (and only) pdfs
        pdf_files = [f for f in os.listdir(self.input_dir) if f[-4:] == ".pdf"]

        if pdf_files:
            return [self.set_password(f) for f in pdf_files]
        else:
            return None

    def export_passwords(self, pws):
        # Export passwords in a text file
        file_name = os.path.split(self.input_dir)[-1]
        with open(os.path.join(self.input_dir, f"{file_name}.txt"), 'a') as file:
            file.writelines(pws)

This is a simple framework for automating the sending of custom emails to businesses.

The settings.json file is where the paths are set to the necessary files in the repo. Git will not add any of these files to its filetree for security reasons. 

	"credentials_path": the path to the csv containing email account credentials, one row.
		Format "EMAIL,PASSWORD"
	"email_metadata_path": 	the path to the csv containing destination emails and institution names, one per row
		Format "EMAIL,
				EMAIL
				..."

	"subject": Subject written directly into settings field as a String.

	"smtp_server": SMTP server written directly into smtp_server field as String.

	"message_path": the path to the custom message txt file.

	"to_replace_csv_path": the path to a single row csv file where each column is another pattern to be replaced. For each pattern in this file, there must be a corresponding replacement pattern of the same index in replaceWith.csv.

	"replace_with_csv_path": the path to csv file where each column is a pattern to replace with. Each row in this file represents an entity to which a custom email will be sent. 



# Valid Date Extractor
This tool is designed to extract valid dates from text in various formats. It supports the following date formats:
* ISO format: `YYYY-MM-DD`
* Slash-separated format: `DD/MM/YYYY`
* Long format: `Month DD, YYYY` , `Mon DD, YYYY`

## Features
- **Flexible date extraction**: Extracts dates in different formats from any text string or text file.
- **Validations**: Only valid dates (in the supported formats) are returned.
- **Efficient**: Extracts and sorts the dates based on their occurrence in the text.

## Supported Date Formats
This tool recognizes and extracts the following date formats:
1. **ISO Format** (`YYYY-MM-DD`):  
   Example: `2023-10-16`
2. **Slash-Separated Format** (`DD/MM/YYYY`):  
   Example: `16/10/2023`
3. **Long Date Format** (`Month DD, YYYY`):  
   Example: `October 16, 2023` or `Oct 16, 2023`


   ```bash
   git clone https://github.com/yourusername/date-extraction-tool.git

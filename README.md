# CityFlow Community Workflows


This repository contains the community workflows for the [Cityflow Platform](https://github.com/kekehurry/cityflow_platform). When the `.csflow.json` files are updated, the `GitHub Action` in this repo will automatically generate the `community_workflows.json` file. The Cityflow platform will then retrieve all community workflows based on the URLs listed in this file. 


## Project Structure

```
my-static-website
│── index.html      # Main HTML file for the static website
│── folder          # datafolder
│   └── data.json   # JSON data file accessible via the website
└── README.md           # Documentation for the project
```

## Getting Started

To set up and run this static website, follow these steps:

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd cityflow_community
   ```

2. **Open the `index.html` File**
   You can open the `index.html` file directly in your web browser. This file serves as the entry point for the website.

3. **Access the JSON Data**
   The JSON data can be accessed directly via the URL:
   ```
   /folder/data.json
   ```

## License

This project is licensed under the MIT License.
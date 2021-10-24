## Library Management System Backend
It's a django based web-app backend of the Library Management System.

### Running on your local computer
You must have **Python** installed on your system.

1. Open **_powershell_** or **_cmd_** and clone the repository:

  ```
  git clone https://github.com/AnasNadeem/library-backend.git
  ```

2. Change the directory 
  ```
  cd library-backend
  ```

3. Create and activate virtual environment.

  For **_Linux_** users:

  ```
  python -m venv env && source ./env/bin/activate
  ```
   
  For **_Windows_** users:
  
  ```
  python -m venv env && .\env\scripts\activate
  ```

4. Install the dependencies from the **_rqrm.txt_**

  ```
  python -m pip install -r rqrm.txt
  ```

5. Run the application

  ```
  python manage.py runserver
  ```


### Directory Structure
  ```
  mysite
  db.sqlite3
  manage.py
  README.md
  rqrm.txt
  ```


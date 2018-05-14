# Back end for General Project

Since the requirement is kind of simple. I choose **Flask** and **MySQL** to implement it.

## Purpose

* Store users and the scores they got in our games

## API

**Get User**

----

Return son data about a single user.

* **URL**

  /users/:uid

* **Method**

  GET

* **URL Params**

  **Required:**

  `uid=[integer]`

  **Optional:**

  `None`

* **Data Params**

  `None`

* **Success Response:**

  * **Code:** 200

    **Content:** 

    ```json
    {
        UID: 100000,
        Username: "Raymond"
    }
    ```

    ​

* **Error Response:**

  * **Code:** 404 NOT FOUND

    **Content:**

    ```json
    {
        error: "User doesn't exist"
    }
    ```

  * **Code:** 401 UNAUTHORIZED

    **Content:**

    ```json
    {
        error: "You are unauthorized to make this request."
    }
    ```

* **Sameple Call**

  `None`

**Sign Up**

----

Create a user.



- **URL**

  /users/

- **Method**

  Post

- **URL Params**

  **Required:**

  `None`

  **Optional:**

  `None`

- **Data Params**

  `Username:[string]`

- **Success Response:**

  - **Code:** 200

    **Content:** 

    ```json
    {
        msg: "Sign up successfully."
    }
    ```

    ​

- **Error Response:**

  - **Code:** 400 BAD REQUEST

    **Content:**

    ```json
    {
        error: "Parameters not found"
    }
    ```

  - **Code:** 401 UNAUTHORIZED

    **Content:**

    ```json
    {
        error: "You are unauthorized to make this request."
    }
    ```

- **Sameple Call**

  `None`
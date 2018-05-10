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

* URL Params

  **Required:**

  `uid=[integer]`

  **Optional:**

  `None`

* Data Params

  `None`

* **Success Response:**

  * Code: 200

    Content: 

    ```json
    {
        UID : 100000,
        Username : "Raymond"
    }
    ```

    ​

* **Error Response:**

  * **Code:** 404 NOT FOUND

    **Content:**

    ```json
    {
        error : "User doesn't exist"
    }
    ```

  * **Code:** 401 UNAUTHORIZED

    **Content:**

    ```json
    {
        error : "You are unauthorized to make this request."
    }
    ```

* **Sameple Call**

  `None`

**TODO**

----


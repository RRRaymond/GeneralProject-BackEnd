# Back end for General Project

Since the requirement is kind of simple. I choose **Flask** and **MySQL** to implement it.

## Purpose

* Store users and the scores they got in our games

## API

**Get User**

----

Return son data about a single user and his scores for 3 games.

* **URL**

  /api/user/

* **Method**

  GET

* **URL Params**

  **Required:**

  `None`

  **Optional:**

  `None`

* **Data Params**

  `None`

* **Success Response:**

  * **Code:** 200 OK

    **Content:** 

    ```json
    {
        "UID": 100000,
        "Username": "Raymond"
        "score": {
            "Game1": 0,
            "Game2": 0,
            "Game3": 0
        }
    }
    ```

    ​

* **Error Response:**

  * **Code:** 404 NOT FOUND

    **Content:**

    ```json
    {
        "error": "User doesn't exist"
    }
    ```

  * **Code:** 401 UNAUTHORIZED

    **Content:**

    ```json
    {
        "error": "You are unauthorized to make this request."
    }
    ```

* **Sameple Call**

  `None`



**Sign Up**

----

Create a user.



- **URL**

  /api/user/

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

  - **Code:** 200 OK

    **Content:** 

    ```json
    {
        "msg": "Sign up successfully."
    }
    ```

    ​

- **Error Response:**

  - **Code:** 400 BAD REQUEST

    **Content:**

    ```json
    {
        "error": "Parameters not found"
    }
    ```

  - **Code:** 401 UNAUTHORIZED

    **Content:**

    ```json
    {
        "error": "You are unauthorized to make this request."
    }
    ```

- **Sameple Call**

  `None`



**Record Score**

----

To record score for a certain user and a certain game.



- **URL**

  /api/score/

- **Method**

  Post

- **URL Params**

  **Required:**

  `None`

  **Optional:**

  `None`

- **Data Params**

  `Score:[INT]`

  `Game:[INT]`

- **Success Response:**

  - **Code:** 200 OK

    **Content:** 

    ```json
    {
        "msg": "Record score successfully."
    }
    ```

    ​

- **Error Response:**

  - **Code:** 400 BAD REQUEST

    **Content:**

    ```json
    {
        "error": "Parameters not found"
    }
    ```

  - **Code:** 401 UNAUTHORIZED

    **Content:**

    ```json
    {
        "error": "You are unauthorized to make this request."
    }
    ```

- **Sameple Call**

  `None`



**Query for LeaderBoard**

------

To get the leaderboard for a certain game.



- **URL**

  /api/score/:game

- **Method**

  GET

- **URL Params**

  **Required:**

  `game:[string]` 

  *game must be one of 'game1', 'game2' or 'game3'*

  **Optional:**

  `None`

- **Data Params**

  `None`

- **Success Response:**

  - **Code:** 200 OK

    **Content:** 

    ```json
    {
      "Content": [
        {
          "Score": 15, 
          "UID": 100015, 
          "Username": "陈胖5"
        }, 
        {
          "Score": 12, 
          "UID": 100011, 
          "Username": "陈钧涛陈胖2"
        }, 
        {
          "Score": 4, 
          "UID": 100013, 
          "Username": "陈钧涛陈胖3"
        }
      ], 
      "Count": 3, 
      "Game": "game3"
    }
    ```

    ​

- **Error Response:**

  - **Code:** 400 BAD REQUEST

    **Content:**

    ```json
    {
        "error": "Parameters not found"
    }
    ```

  - **Code:** 401 UNAUTHORIZED

    **Content:**

    ```json
    {
        "error": "You are unauthorized to make this request."
    }
    ```

- **Sameple Call**

  `None`


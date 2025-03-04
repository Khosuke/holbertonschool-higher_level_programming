# Project: SQL - More Queries

## Task 0. My privileges!
Write a script that lists all privileges of the MySQL users ``user_0d_1`` and ``user_0d_2`` on your server (in localhost).
File: 0-privileges.sql

## Task 1. Root user
Write a script that creates the MySQL server user ``user_0d_1``.
- ``user_0d_1`` should have all privileges on your MySQL server
- The ``user_0d_1`` password should be set to ``user_0d_1_pwd``
File: 1-create_user.sql

## Task 2. Read user
Write a script that creates the database ``hbtn_0d_2`` and the user ``user_0d_2``.
- ``user_0d_2`` should have only SELECT privilege in the database ``hbtn_0d_2``
- The ``user_0d_2`` password should be set to ``user_0d_2_pwd``
File: 2-create_read_user.sql

## Task 3. Always a name
Write a script that creates the table ``force_name`` on your MySQL server.
- ``force_name`` description:
    - ``id`` INT
    - ``name`` VARCHAR(256) can’t be null
File: 3-force_name.sql

## Task 4. ID can't be null
Write a script that creates the table ``id_not_null`` on your MySQL server.
- ``id_not_null`` description:
    - ``id`` INT with the default value 1
    - ``name`` VARCHAR(256)
File: 4-never_empty.sql

## Task 5. Unique ID
Write a script that creates the table ``unique_id`` on your MySQL server.
- ``unique_id`` description:
    - ``id`` INT with the default value 1 and must be unique
    - ``name`` VARCHAR(256)
File: 5-unique_id.sql

## Task 6. States table
Write a script that creates the database ``hbtn_0d_usa`` and the table ``states`` (in the database ``hbtn_0d_usa``) on your MySQL server.
- ``states`` description:
    - ``id`` INT unique, auto generated, can’t be null and is a primary key
    - ``name`` VARCHAR(256) can’t be null
File: 6-states.sql

## Task 7. Cities table
Write a script that creates the database ``hbtn_0d_usa`` and the table ``cities`` (in the database ``hbtn_0d_usa``) on your MySQL server.
- ``cities`` description:
    - ``id`` INT unique, auto generated, can’t be null and is a primary key
    - ``state_id`` INT, can’t be null and must be a FOREIGN KEY that references to id of the states table
    - ``name`` VARCHAR(256) can’t be null
File: 7-cities.sql

## Task 8. Cities of California
Write a script that lists all the cities of California that can be found in the database ``hbtn_0d_usa``.
- The ``states`` table contains only one record where ``name`` = ``California`` (but the id can be different, as per the example)
- Results must be sorted in ascending order by ``cities.id``
File: 8-cities_of_california_subquery.sql

## Task 9. Cities by States
Write a script that lists all cities contained in the database ``hbtn_0d_usa``.
- Each record should display: ``cities.id`` - ``cities.name`` - ``states.name``
- Results must be sorted in ascending order by ``cities.id``
File: 9-cities_by_state_join.sql

## Task 10. Genre ID by show
Write a script that lists all shows contained in ``hbtn_0d_tvshows`` that have at least one genre linked.
- Each record should display: ``tv_shows.title`` - ``tv_show_genres.genre_id``
- Results must be sorted in ascending order by ``tv_shows.title`` and ``tv_show_genres.genre_id``
File: 10-genre_id_by_show.sql

## Task 11. Genre ID for all shows
Write a script that lists all shows contained in the database ``hbtn_0d_tvshows``.
- Each record should display: ``tv_shows.title`` - ``tv_show_genres.genre_id``
- Results must be sorted in ascending order by ``tv_shows.title`` and ``tv_show_genres.genre_id``
- If a show doesn’t have a genre, display ``NULL``
File: 11-genre_id_all_shows.sql

## Task 12. No genre
Write a script that lists all shows contained in ``hbtn_0d_tvshows`` without a genre linked.
- Each record should display: ``tv_shows.title`` - ``tv_show_genres.genre_id``
- Results must be sorted in ascending order by ``tv_shows.title`` and ``tv_show_genres.genre_id``
File: 12-no_genre.sql

## Task 13. Number of shows by genre
Write a script that lists all genres from ``hbtn_0d_tvshows`` and displays the number of shows linked to each.
- Each record should display: ``<TV Show genre>`` - ``<Number of shows linked to this genre>``
- First column must be called ``genre``
- Second column must be called ``number_of_shows``
- Don’t display a genre that doesn’t have any shows linked
- Results must be sorted in descending order by the number of shows linked
File: 13-count_shows_by_genre.sql

## Task 14. My genres
Write a script that uses the ``hbtn_0d_tvshows`` database to lists all genres of the show ``Dexter``.
- The ``tv_shows`` table contains only one record where ``title`` = ``Dexter`` (but the ``id`` can be different)
- Each record should display: ``tv_genres.name``
- Results must be sorted in ascending order by the genre name
File: 14-my_genres.sql

## Task 15. Only Comedy
Write a script that lists all Comedy shows in the database ``hbtn_0d_tvshows``.
- The ``tv_genres`` table contains only one record where ``name`` = ``Comedy`` (but the ``id`` can be different)
- Each record should display: ``tv_shows.title``
- Results must be sorted in ascending order by the show title
File: 15-comedy_only.sql

## Task 16. List shows and genres
Write a script that lists all shows, and all genres linked to that show, from the database ``hbtn_0d_tvshows``.
- If a show doesn’t have a genre, display ``NULL`` in the genre column
- Each record should display: ``tv_shows.title`` - ``tv_genres.name``
- Results must be sorted in ascending order by the show title and genre name
File: 16-shows_by_genre.sql

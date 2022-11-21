# Constant Time

## What is it?

Site to keep track of progress on various judge websites and reward users for:

* Trying harder problems
* Continuously trying problems
* Trying new problem types

## How is this done?

* Weekly Problems with increased Rewards (Streak Freezes) means that certain "Just tough enough" problems can be selected to extend your ability (And not require you to log in every day)
* Shared Problem Groups allow you to collaborate with peers in realtime and replay existing contests that start at inopportune times
* Motivate writing well written solutions and explanations by incorporating an upvote system and giving prizes for commonly upvoted explanations

## What does the site currently do?

* Keep track of your current problem streak on CodeForces
* Give an in-site editor to CodeForces problems, and show your streak on a calendar
* Keep track of coins + streak freezes

## What needs to be done on the site?

* Fix login
* Allow users to user streak freezes by clicking on the calendar
* Show extra information on problem submission
* Support Shared Problem Groups / Friending
* Support Leaderboards and Graph problem stats on submission
* Make it look good
* Link with more sites

## Other important info

* Almost everything on this site regarding other vendors, such as codeforces, is client-authoratative. This is simply a requirement due to the rate-limiting of the CF API. This is fine, provided everyone plays by the rules


# Development

## Installation

* Requires Python 3.9+
* Requires NPM
* Requires PostgreSQL installed, and a database created
    * Either make the database/user specified in `server/server/settings.py` in the DASHBOARD item, OR
    * Make a new DASHBOARD dictionary in `server/server/local_settings.py`

Run `install.sh` to install.

## Running the instance

* Frontend: Must be built before Backend with `cd client`, `npm run serve`
* Backend: `cd server`, `python manage.py runserver`

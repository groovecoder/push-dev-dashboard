Deployment
==========

moz-dev-dash is designed with `12-factor app philosophy`_ to run on `heroku`_, so you
can easily deploy your changes to your own heroku app with `heroku toolbelt`_.


Deploy your own
---------------

#. `Create a heroku remote`_. We suggest naming it moz-dev-dash-`username`::

    heroku apps:create moz-dev-dash-username

#. Push code to the heroku remote::

    git push heroku master

#. `Migrate`_ DB tables on heroku::

    heroku run python manage.py migrate

#. Create a superuser on heroku::

    heroku run python manage.py createsuperuser

#. Open the new heroku app::

    heroku open

Enable Firefox Accounts Auth on Heroku
--------------------------------------

To enable Firefox Account sign-ins on your heroku app, you will need to create
your own Firefox Accounts OAuth Client for your app domain.

#. Go to `register your own Firefox Accounts OAuth Client`_:

    * Client name: moz-dev-dash-username
    * Redirect URI: https://moz-dev-dash-username.herokuapp.com/accounts/fxa/login/callback/
    * Trusted Mozilla Client: **CHECKED**

   Be sure to copy the client secret - you can't see it again.

#. Go to https://moz-dev-dash-username.herokuapp.com/admin/socialaccount/socialapp/add/
   to :ref:`enable Firefox Accounts Auth` like a local machine; this time using your own new Firefox Accounts OAuth Client ID and Secret

#. Sign in at https://moz-dev-dash-username.herokuapp.com/ with a Firefox
   Account.

Enable Untappd Auth on Heroku
--------------------------------------

To enable Untappd sign-ins on your heroku app, you will need to create
your own Untappd OAuth Client for your app domain.

#. Go to `register your own Untappd OAuth Client`_:

    * Client name: moz-dev-dash-username
    * Redirect URI: https://moz-dev-dash-username.herokuapp.com/accounts/untappd/login/callback/

   Be sure to copy the client secret - you can't see it again.

#. Go to https://moz-dev-dash-username.herokuapp.com/admin/socialaccount/socialapp/add/
   to :ref:`enable Untappd Auth` like a local machine; this time using your own new untappd OAuth Client ID and Secret

#. Sign in at https://moz-dev-dash-username.herokuapp.com/ with a Untappd
   Account.

.. _12-factor app philosophy: http://12factor.net/
.. _heroku toolbelt: https://toolbelt.heroku.com/
.. _Create a heroku remote: https://devcenter.heroku.com/articles/git#creating-a-heroku-remote
.. _register your own Untappd OAuth Client: https://untappd.com/api/register

.. _heroku: https://www.heroku.com/
.. _git hooks: http://git-scm.com/book/en/Customizing-Git-Git-Hooks
.. _balanced.js: https://github.com/balanced/balanced-js

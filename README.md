# LinkedIn Automator 🚀

A Python-based automation tool that streamlines publishing content to
LinkedIn. Run the main script and the application handles the workflow,
including selecting content from a local folder, checking
authentication, obtaining authorization when required, and submitting
the post through LinkedIn's API.

## Features

-   **Automated execution:** Start the workflow from `main.py`.
-   **File handling:** Selects content from the configured local folder.
-   **OAuth 2.0 authentication:** Uses LinkedIn's authorization flow.
-   **Local callback server:** Receives the authorization response
    through a local HTTP server.
-   **Token handling:** Checks the stored token and handles the
    authorization flow when a new token is needed.
-   **LinkedIn API integration:** Sends the post request to LinkedIn and
    processes the API response.
-   **Configuration-based setup:** Keeps application settings and
    credentials outside the main Python code.

## Project structure

``` text
Linkedin automator/
├── .gitignore
├── README.md
├── main.py
├── auth.py
├── complete_auth.py
├── expiry.py
├── linkedin_token.py
├── server.py
├── codes.ini
├── key.env
├── day.txt
├── draft.txt
└── prompt.txt
```

`__pycache__/` and temporary editor files are omitted because they are
generated locally and are not part of the application source.

### Main files

  -----------------------------------------------------------------------
  File                                Purpose
  ----------------------------------- -----------------------------------
  `main.py`                           Entry point that starts the
                                      automation workflow.

  `auth.py`                           Authentication-related logic.

  `complete_auth.py`                  Completes the LinkedIn
                                      authorization/token flow.

  `expiry.py`                         Handles token-expiry checks or
                                      related date calculations.

  `linkedin_token.py`                 LinkedIn token-related operations.

  `server.py`                         Local HTTP callback server used
                                      during authorization.

  `codes.ini`                         Stores application
                                      state/configuration such as
                                      authorization or token data.

  `key.env`                           Stores environment variables and
                                      API credentials.

  `draft.txt`                         Draft content used by the workflow.

  `prompt.txt`                        Prompt/instructions used by the
                                      application.

  `day.txt`                           Local date/day state used by the
                                      workflow.
  -----------------------------------------------------------------------

## How it works

1.  Run `main.py`.
2.  The application selects the content file from the configured
    folder/workflow.
3.  It checks the stored LinkedIn authentication details.
4.  If authorization is needed, the local callback server receives the
    authorization code.
5.  The application exchanges the code for an access token and stores
    the required token data.
6.  The application sends the post to LinkedIn using an authenticated
    API request.
7.  The application checks LinkedIn's response to determine whether the
    request succeeded.

## Requirements

-   Python 3
-   A LinkedIn account
-   A LinkedIn Developer application with the required API
    product/permissions
-   The redirect URI configured in the LinkedIn Developer application
    must match the URI used by this project

Install the external Python packages used by the project:

``` bash
pip install requests python-dotenv google-genai
```

The project also uses Python standard-library modules, including
`http.server`, `urllib`, `configparser`, and `os`.

## Configuration

1.  Create/configure your LinkedIn application in the [LinkedIn
    Developer Portal](https://www.linkedin.com/developers/).
2.  Configure the OAuth redirect URL used by your local callback server.
3.  Add the required credentials and API keys to `key.env`.
4.  Configure the required values in `codes.ini` as expected by the
    application.
5.  Ensure the LinkedIn application has the permissions required for the
    API operations used by the project.

Do not copy real credentials into this README or commit them to a public
repository.

## Run the project

From the project directory, run:

``` bash
python main.py
```

Follow the browser authorization step if the application requests it.
Once authorization is complete, the application continues with the
configured publishing workflow.

## Security notes

-   Keep `key.env` out of version control.
-   Do not publish your LinkedIn client secret, access token, refresh
    token, authorization code, or other credentials.
-   Check that `.gitignore` excludes all credential files and any local
    files containing tokens.
-   If a credential has been committed publicly, revoke or rotate it
    immediately.

## Limitations and notes

-   LinkedIn API access and publishing permissions depend on the
    LinkedIn Developer application and the permissions granted to it.
-   Access-token lifetime and renewal behavior depend on the LinkedIn
    OAuth configuration. The application may require the user to
    authorize again when a valid token cannot be renewed.
-   A successful HTTP response should be checked by the application; a
    request being sent does not by itself guarantee that a post was
    published.

## Author

**Pulkit Gupta**

Built to practise Python automation, OAuth 2.0, HTTP servers, API
integration, configuration management, and file handling.

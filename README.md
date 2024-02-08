# GitHub Social Graph
Introducing **GitHub Social Graph**, a sophisticated analytical tool designed to intricately map and dissect the social connectivity landscape on GitHub. At its core, GitHub Social Graph empowers users to delve into the nuanced dynamics of follower and following relationships, offering an unprecedented level of insight into the interactive webs that bind the GitHub community.

This tool is meticulously designed to cater to developers, researchers, and enthusiasts who seek a deeper understanding of their GitHub social network. By providing detailed comparisons of followers and followings for individual users, GitHub Social Graph reveals the intricate patterns of connectivity, highlighting mutual connections and uncovering the broader implications of these relationships within the GitHub ecosystem.

Key Features of GitHub Social Graph include:

- **Follower and Following Analysis:** Instantaneously compare the followers and following lists of a GitHub user, identifying unique and mutual connections with precision and clarity.
- **Mutual Connection Discovery:** Effortlessly find mutual connections between multiple users, offering valuable insights into collaborative networks and potential avenues for future partnerships or projects.

Whether you're aiming to expand your professional network, seeking collaborators for open-source projects, or simply curious about your position within the vast GitHub community, GitHub Social Graph serves as your gateway to a deeper understanding of social interactions on one of the world's largest platforms for developers.

GitHub Social Graph stands as a testament to the power of community and connectivity in the digital age, offering users a unique lens through which to view their online interactions. Welcome to a new era of social analytics on GitHub, where insights into your digital connections are just a few clicks away.

## Usage

```
python main.py --help
usage: main.py [-h] [-u USERNAME] [--orgs] [--users USERS USERS]

A CLI tool to know about GitHub social connections.

options:
  -h, --help            show this help message and exit
  -u USERNAME, --username USERNAME
                        Username to compare followers and following. Example: --username octocat
  --orgs                Include organizations in the comparison. Example: --orgs
  --users USERS USERS   Two users to compare mutual connections. Example: --users octocat hubot

```

### 1. Comparing Followers and Following
```
python main.py --username sample
```
Returns a tabulated comparison of the followers and following of the user `sample`.
```
People who sample don't follow back (27):
+-------------------+--------------------------------------+
| username          | html_url                             |
+===================+======================================+
| alexundros        | https://github.com/alexundros        |
+-------------------+--------------------------------------+
| angusshire        | https://github.com/angusshire        |
+-------------------+--------------------------------------+
| DiamondAdaeze-MBA | https://github.com/DiamondAdaeze-MBA |
+-------------------+--------------------------------------+
| dkhabarov         | https://github.com/dkhabarov         |
+-------------------+--------------------------------------+
| geraldo-netto     | https://github.com/geraldo-netto     |
+-------------------+--------------------------------------+
| giko              | https://github.com/giko              |
+-------------------+--------------------------------------+
| gooddavvy         | https://github.com/gooddavvy         |
+-------------------+--------------------------------------+
| h0st              | https://github.com/h0st              |
+-------------------+--------------------------------------+
| JosuaSitorus      | https://github.com/JosuaSitorus      |
+-------------------+--------------------------------------+
| JuliaVenzh        | https://github.com/JuliaVenzh        |
+-------------------+--------------------------------------+
| KabiruA159        | https://github.com/KabiruA159        |
+-------------------+--------------------------------------+
| lcuevastodoit     | https://github.com/lcuevastodoit     |
+-------------------+--------------------------------------+
| lennakz           | https://github.com/lennakz           |
+-------------------+--------------------------------------+
| Lisprez           | https://github.com/Lisprez           |
+-------------------+--------------------------------------+
| litesheng         | https://github.com/litesheng         |
+-------------------+--------------------------------------+
| maliqq            | https://github.com/maliqq            |
+-------------------+--------------------------------------+
| MichalPaszkiewicz | https://github.com/MichalPaszkiewicz |
+-------------------+--------------------------------------+
| Mohamed988o       | https://github.com/Mohamed988o       |
+-------------------+--------------------------------------+
| morlofff          | https://github.com/morlofff          |
+-------------------+--------------------------------------+
| nellaivijay       | https://github.com/nellaivijay       |
+-------------------+--------------------------------------+
| nhattri           | https://github.com/nhattri           |
+-------------------+--------------------------------------+
| Osamankapit       | https://github.com/Osamankapit       |
+-------------------+--------------------------------------+
| ptqa              | https://github.com/ptqa              |
+-------------------+--------------------------------------+
| R3dFruitRollUp    | https://github.com/R3dFruitRollUp    |
+-------------------+--------------------------------------+
| Spaceinvaderz     | https://github.com/Spaceinvaderz     |
+-------------------+--------------------------------------+
| Tae1998           | https://github.com/Tae1998           |
+-------------------+--------------------------------------+
| Uburwator         | https://github.com/Uburwator         |
+-------------------+--------------------------------------+


 People who don't follow sample back (28):
+-----------------+------------------------------------+
| username        | html_url                           |
+=================+====================================+
| arr-ee          | https://github.com/arr-ee          |
+-----------------+------------------------------------+
| bioothod        | https://github.com/bioothod        |
+-----------------+------------------------------------+
| bobuk           | https://github.com/bobuk           |
+-----------------+------------------------------------+
| czm41k          | https://github.com/czm41k          |
+-----------------+------------------------------------+
| dragonsmith     | https://github.com/dragonsmith     |
+-----------------+------------------------------------+
| drduh           | https://github.com/drduh           |
+-----------------+------------------------------------+
| evtuhovich      | https://github.com/evtuhovich      |
+-----------------+------------------------------------+
| fnichol         | https://github.com/fnichol         |
+-----------------+------------------------------------+
| jtimberman      | https://github.com/jtimberman      |
+-----------------+------------------------------------+
| kirs            | https://github.com/kirs            |
+-----------------+------------------------------------+
| kobolog         | https://github.com/kobolog         |
+-----------------+------------------------------------+
| kovyrin         | https://github.com/kovyrin         |
+-----------------+------------------------------------+
| legal90         | https://github.com/legal90         |
+-----------------+------------------------------------+
| makaroni4       | https://github.com/makaroni4       |
+-----------------+------------------------------------+
| michaelklishin  | https://github.com/michaelklishin  |
+-----------------+------------------------------------+
| mszoernyi       | https://github.com/mszoernyi       |
+-----------------+------------------------------------+
| natikgadzhi     | https://github.com/natikgadzhi     |
+-----------------+------------------------------------+
| nordringrayhide | https://github.com/nordringrayhide |
+-----------------+------------------------------------+
| osminog         | https://github.com/osminog         |
+-----------------+------------------------------------+
| prepor          | https://github.com/prepor          |
+-----------------+------------------------------------+
| SaveTheRbtz     | https://github.com/SaveTheRbtz     |
+-----------------+------------------------------------+
| smith3v         | https://github.com/smith3v         |
+-----------------+------------------------------------+
| timurb          | https://github.com/timurb          |
+-----------------+------------------------------------+
| tukan           | https://github.com/tukan           |
+-----------------+------------------------------------+
| vadv            | https://github.com/vadv            |
+-----------------+------------------------------------+
| verm666         | https://github.com/verm666         |
+-----------------+------------------------------------+
| vlm             | https://github.com/vlm             |
+-----------------+------------------------------------+
| whitew1nd       | https://github.com/whitew1nd       |
+-----------------+------------------------------------+


 Mutual followers for sample (12):
+------------+------------------------------+
| username   | html_url                     |
+============+==============================+
| AlekSi     | https://github.com/AlekSi    |
+------------+------------------------------+
| bitle      | https://github.com/bitle     |
+------------+------------------------------+
| Chhed13    | https://github.com/Chhed13   |
+------------+------------------------------+
| iroller    | https://github.com/iroller   |
+------------+------------------------------+
| kavu       | https://github.com/kavu      |
+------------+------------------------------+
| m9         | https://github.com/m9        |
+------------+------------------------------+
| nabam      | https://github.com/nabam     |
+------------+------------------------------+
| pcheliniy  | https://github.com/pcheliniy |
+------------+------------------------------+
| serjs      | https://github.com/serjs     |
+------------+------------------------------+
| skotopes   | https://github.com/skotopes  |
+------------+------------------------------+
| xeron      | https://github.com/xeron     |
+------------+------------------------------+
| yaroslav   | https://github.com/yaroslav  |
+------------+------------------------------+
Total followers for sample: 39
Total following sample: 40
```

### 2. Comparing Mutual Connections
```
python main.py --users thearjun aashisham
```

Returns a tabulated comparison of the mutual connections between the users `thearjun` and `aashisham`.
```
 python main.py --users thearjun aashisham


People who (thearjun, aashisham) both follow:
+----------------+-----------------------------------+
| username       | html_url                          |
+================+===================================+
| ananta         | https://github.com/ananta         |
+----------------+-----------------------------------+
| bishwasojha    | https://github.com/bishwasojha    |
+----------------+-----------------------------------+
| IamDiwash      | https://github.com/IamDiwash      |
+----------------+-----------------------------------+
| khoms          | https://github.com/khoms          |
+----------------+-----------------------------------+
| kusalmagar     | https://github.com/kusalmagar     |
+----------------+-----------------------------------+
| parajuliamit   | https://github.com/parajuliamit   |
+----------------+-----------------------------------+
| pradishb       | https://github.com/pradishb       |
+----------------+-----------------------------------+
| sachinshilwal  | https://github.com/sachinshilwal  |
+----------------+-----------------------------------+
| SagarPaudel    | https://github.com/SagarPaudel    |
+----------------+-----------------------------------+
| sandeshstha    | https://github.com/sandeshstha    |
+----------------+-----------------------------------+
| sumanbhattarai | https://github.com/sumanbhattarai |
+----------------+-----------------------------------+
| SunilGolden    | https://github.com/SunilGolden    |
+----------------+-----------------------------------+
| Talank         | https://github.com/Talank         |
+----------------+-----------------------------------+
| theoriginalsam | https://github.com/theoriginalsam |
+----------------+-----------------------------------+
| tseevag        | https://github.com/tseevag        |
+----------------+-----------------------------------+
```


## Architecuture of GitHub Social Graph

### 1. Project Structure

```
github-social-graph/
│
├── main.py                           # Main application script
│
├── services/                         # Business logic
│   ├── __init__.py
│   ├── comparison_service.py         # Compares followers and following
│   ├── mutual_connection_service.py  # Tabulates the mutual connections
│   └── tabulate_service.py           # Tabulates the comparison results
│
├── controllers/                      # Entry point for handling requests
│   ├── __init__.py
│   ├── compare.py                    # Compares followers and following
│   └── mutual.py                     # Gets mutual connections
│
├── models/                           # Data models
│   ├── __init__.py
│   ├── user.py                       # User model
│   ├── difference.py                 # Difference model
│   └── mutual_connection.py          # Mutual Connection model
│
├── repositories/                     # Data access layer
│   ├── __init__.py
│   └── github_repository.py          # Abstraction over GitHub data fetching
│
├── utils/                            # Utility functions and classes
│   ├── __init__.py
│   ├── network.py                    # Network related utilities
│   └── parsers.py                    # Argument parsers
```

### 2. Components

#### 2.1 Main Application (`main.py`)
- Entry point of the application.
- Initializes and orchestrates the service layer.

#### 2.2 Services (`services/`)
- **Comparison Service (`comparison_service.py`):** Contains the logic to compare followers and following lists, determining the differences.
- **Tabulate Service (`tabulate_service.py`):** Handles the tabulation of comparison results, formatting the data for display or further processing.
- **Mutual Connection Service (`mutual_connection_service.py`):** Provides the logic to find mutual connections between users.

#### 2.3 Models (`models/`)
- Define data structures.
- **User (`user.py`):** Represents a GitHub user, including necessary attributes like username, followers, and following.
- **Difference (`difference.py`):** Represents the difference in followers and following, used to encapsulate the result of comparisons.
- **Mutual Connection (`mutual_connection.py`):** Represents a mutual connection between two users.

#### 2.4 Repositories (`repositories/`)
- **GitHub Repository (`github_repository.py`):** Acts as a data access layer that directly communicates with GitHub's API, abstracting away the specifics of data fetching. This allows for easier testing and changes to the data source.

#### 2.5 Utilities (`utils/`)
- **Network Utilities (`network.py`):** Includes helpers for network requests, error handling, and response parsing to ensure that service components interact with external APIs robustly.
- **Parsers (`parsers.py`):** Contains argument parsers for command-line input, ensuring that the application can be easily configured and used.

#### 2.6 Controllers (`controllers/`)
- **Compare (`compare.py`):** Handles requests to compare followers and following.
- **Mutual (`mutual.py`):** Handles requests to find mutual connections.

### 3. Key Design Principles

- **Low Coupling:** Each component has a clear, defined purpose, interacting with others through well-defined interfaces. This allows for easier maintenance and testing.
- **High Cohesion:** Related functionalities are grouped together, promoting reusability and modularity.
- **Abstraction:** The repository layer abstracts the complexity of network calls and API interactions, allowing services to focus on business logic.
- **Testing:** Each layer is independently testable, facilitating unit tests for logic-heavy services and integration tests that involve network interactions.

### 4. Workflow

1. **Request Handling:** The application receives a request to compare a user's followers and following.
2. **Service Layer:** The main application invokes the GitHub service to fetch the necessary data using the GitHub repository.
3. **Data Fetching:** The GitHub repository interacts with GitHub's API, fetching the follower and following data.
4. **Comparison:** The fetched data is passed to the Comparison service, which calculates the differences.
5. **Response Generation:** The application returns the comparison results.

This architecture provides a solid foundation for building a Python project focused on GitHub data analysis, ensuring that it's maintainable, scalable, and easily testable.

When incorporating GitHub API authentication via personal access tokens into your project, it's crucial to provide clear documentation for users or developers on how to generate and use these tokens. Below is a sample README section that explains the process of obtaining and configuring a GitHub token (`MY_GITHUB_TOKEN`) for use with your application.

---

## Configuring GitHub API Authentication

This project interacts with the GitHub API and supports authentication using personal access tokens to increase the API rate limit and access private repositories. To use this feature, you'll need to create a GitHub token and configure the application to use it.

### Generating a GitHub Personal Access Token

Follow these steps to generate a personal access token on GitHub:

1. Log in to your GitHub account.
2. Go to Settings > Developer settings > Personal access tokens.
3. Click on "Generate new token".
4. Give your token a descriptive name under "Note".
5. Select the scopes or permissions you'd like to grant this token. For public repositories, checking `public_repo` is often sufficient. For access to private repositories, you may need to select additional scopes.
6. Click "Generate token" at the bottom of the page.
7. **Important:** Copy the token to a secure place. GitHub won't show the token again once you navigate away from the page.

### Configuring the Token in the Application

After generating your personal access token, you need to make it available to the application without exposing it in the source code. The recommended approach is to use environment variables.

#### Setting the Environment Variable

- **For Unix/Linux/macOS:**
  
  Open your terminal and enter the following command (replace `YOUR_TOKEN_HERE` with the token you generated):

  ```sh
  export MY_GITHUB_TOKEN=YOUR_TOKEN_HERE
  ```

  To make this change permanent, add the command to your shell's startup file, like `~/.bashrc` or `~/.zshrc`.

- **For Windows:**

  Open Command Prompt as an administrator and enter the following command (replace `YOUR_TOKEN_HERE` with the token you generated):

  ```cmd
  setx MY_GITHUB_TOKEN "YOUR_TOKEN_HERE"
  ```

  Note: This adds the environment variable permanently. You might need to restart your command prompt or IDE for the changes to take effect.

#### Accessing the Token in the Application

Ensure your application is configured to read the `MY_GITHUB_TOKEN` environment variable. For example, in `main.py`, we have used as:

```python
import os

MY_GITHUB_TOKEN = os.getenv('MY_GITHUB_TOKEN')
```

### Security Considerations

- **Never hard-code your personal access token** within your application's source code, especially if you're sharing the code publicly.
- Regularly review and rotate your tokens to ensure they haven't been compromised.
- Adhere to GitHub's best practices for token security, including minimal scope assignment.

For more information on GitHub tokens and their security, visit [GitHub's official documentation](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token).

---

This section provides essential information on generating, configuring, and securely using a GitHub personal access token with your project. Adjust the documentation as necessary to match your project's specific configuration and requirements.

# bublikum-bot
- [Discord Server](https://discord.gg/HsaYVHgSst)
- [Docker Site](https://hub.docker.com/repository/docker/tcgmilan/bublikum-bot)


## Configuration
  Check for `settings.ini`   
### Variables
- `$date`: Replaces with current date. Format: `settings.ini`
- `$target`: Command target (mostly mentioned first)
- `$author`: Command author  


## Start Bot
1. Create `.env` file inside directory
2. Insert: `TOKEN=<token>`
3. [Windows]   
Run: `pip install -r requirements.txt && python .`     

   [Linux/ OSX]   
Run: `pip3 install -r requirements.txt && python3 .`


## Docker Setup
1. [Download Docker](https://www.docker.com/get-started)
2. Run: `docker run -e TOKEN=<token> -d tcgmilan/bublikum-bot`

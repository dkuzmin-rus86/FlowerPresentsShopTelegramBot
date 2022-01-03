# FlowerPresentsShop - Telegram Bot
An example of a Telegram Bot for creating and promoting a catalog of a flower shop with photos, descriptions, prices. The telegram bot has a client menu and an administrator menu for adding and removing flower bouquets to the database.

1. Rename .env_local to .env
```bash
mv .env_local .env
```
2. Set TELEGRAM_API_TOKEN in .env file

3. Create docker image
```bash
docker build -t flowershopimage ./
```

4. Run docker container
```bash
docker run -d --name flower flowershopimage
```

virtualenv -p python3 phone_book_env
source phone_book_env/bin/activate
pip install -r requirements.txt


wget http://download.redis.io/releases/redis-5.0.4.tar.gz
tar xzf redis-5.0.4.tar.gz
cd redis-5.0.4
make
cd ..
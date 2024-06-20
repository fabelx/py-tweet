# Python Tweet

![PyPI - Version](https://img.shields.io/pypi/v/python-tweet?labelColor=%232e343b&label=pypi%20package)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/python-tweet?labelColor=%232e343b)
![PyPI - License](https://img.shields.io/pypi/l/python-tweet?labelColor=%232e343b)
[![Tests](https://github.com/fabelx/py-tweet/actions/workflows/tests.yml/badge.svg)](https://github.com/fabelx/py-tweet/actions/workflows/tests.yml)


## About
`pytweet` is a simple Python library with one goal: to retrieve tweet information from **X** for free.

_Inspired by [React-tweet](https://github.com/vercel/react-tweet) project._

### Key Feature
- doesn't require an [X](https://x.com/) (formerly known as **Twitter**) API token
___

## Installation
```bash
pip install python-tweet
```
From source:
```bash
make install
```
or
```bash
pip install .
```
___

## Usage
> ### It may cause conflicts with [PyTweet](https://pypi.org/project/PyTweet/) if you are using it in your project.

#### Async way:
```python
import asyncio
import json

from pytweet import get_tweet


async def main():
    tweet_id = "1803774806980022720"
    data = await get_tweet(tweet_id)
    with open(f"{tweet_id}.json", "w") as f:
        json.dump(data, f, indent=2)


if __name__ == '__main__':
    asyncio.run(main())

```

#### Sync way:
```python
import json

from pytweet.sync import get_tweet


def main():
    tweet_id = "1803774806980022720"
    data = get_tweet(tweet_id)
    with open(f"{tweet_id}.json", "w") as f:
        json.dump(data, f, indent=2)


if __name__ == '__main__':
    main()

```
___

### To-do
- [ ] Return a Tweet class instead a raw dict.
___

## License
`python-tweet` is released under the MIT License.
See the [LICENSE](https://github.com/fabelx/pycrossword/blob/main/LICENSE) file for license information.

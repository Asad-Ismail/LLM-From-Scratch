# LLM-from-Scratch
Implementing LLM training from scratch


## Tokenizer

See example:
https://tiktokenizer.vercel.app/
https://www.youtube.com/watch?v=zduSFxRajkE&t=304s


Many of the artifacts or not perfomining good in particular cases can be traced back to tokenizers (e.g some time llms being bad at math or spelling). Same words can be tokenized into different tokens depending on its location in sentence and also capital or small letter for GPT2 tokenizer. Numbers can be arbitrarily broken up also by tokeinizer. For the languages the llm has not seen during training, we tend to get lot more tokens for same sentence in english this results in bloated context size for foreign languages. GPT4 tokenizer produce half as many tokens as GPT2 tokenizer which is a good thing as same text is squished in half and we can double the context size, but it also inclreases the vocab size and now embedding table also grows and softamx is over more higher dimensions. String in python are unicode codepoints, we can get it using ord function in python. We donot use unicode representation directly because first it has more than 150,000 code points and seconly it keeps changing as it is a chaning standard. To have a more stable representation we encode unicode code point to UTF 8 encoding which is variable byte encoding. it converts ints to bytes. Just utf8 encoding will produce ver long encodings and need very large context because vocab size is only 256 as are the bytes but have variabel length. So we need to trade the vocab size with encoding length.
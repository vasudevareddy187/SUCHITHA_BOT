from pyrogram import Client, filters
from pyrogram.types import Message
import asyncio
import random, re
import requests 



# --------------------------------------------------------------------------------- #

MEME_IMG = (
   "https://telegra.ph/file/fd0be06d2da20771b3016.jpg",
   "https://telegra.ph/file/cbf51a9974caf347a3057.jpg",
   "https://telegra.ph/file/2767b0c98f122dabe930f.jpg",
   "https://telegra.ph/file/31dd04c2b0ee0a661b23e.jpg",
   "https://telegra.ph/file/ad9a2cfeca56a05804a62.jpg",
   "https://telegra.ph/file/e67e384c40e964b0a4aa1.jpg",
   "https://telegra.ph/file/d2edca7d0f401d2c3c72d.jpg",
   "https://telegra.ph/file/7e41e8035d141f9057e98.jpg",
   "https://telegra.ph/file/0fe016f2b3d604277e7a8.jpg",
   "https://telegra.ph/file/b27ea9a1ac78a6a2edcdd.jpg",
   "https://telegra.ph/file/e1c5e3b6274438bc6ac4b.jpg",
   "https://telegra.ph/file/0bb8477ab0e4b40505854.jpg",
   "https://telegra.ph/file/06232497dda4405f24bd4.jpg",
   "https://telegra.ph/file/e16b9bf5cbc76758127fc.jpg",
   "https://telegra.ph/file/2b25931e3b91aa7acf536.jpg",
   "https://telegra.ph/file/3bcdb6ab83300deee9113.jpg",
   "https://telegra.ph/file/6ea1c47159d5a8029ca50.jpg",
   "https://telegra.ph/file/6dc6ea6910f846b25d99c.jpg",
   "https://telegra.ph/file/ce315dd760d5e3cd8344d.jpg",
   "https://telegra.ph/file/5571d2542065ee0fc6c16.jpg",
   "https://telegra.ph/file/7e79b3620f6b5aab1d633.jpg",
   "https://telegra.ph/file/096e03f8c2588bdc501b3.jpg",
   "https://telegra.ph/file/be6a9e8bbb7aa4713882f.jpg",
   "https://telegra.ph/file/66c9c8661181ef33d2d56.jpg",
   "https://telegra.ph/file/172a23cedf9aba731d14e.jpg",
   "https://telegra.ph/file/26c5a58900fd07e1e19eb.jpg",
   "https://telegra.ph/file/13621caf5989e61966109.jpg",
   "https://telegra.ph/file/47a8d33bc256362de1b6b.jpg",
   "https://telegra.ph/file/862fbab8c2d7dc2f88813.jpg",
   "https://telegra.ph/file/09f02dc696ea6b34fb164.jpg",
   "https://telegra.ph/file/c644158b9a8428e2296b3.jpg",
   "https://telegra.ph/file/1c8bd4b41fc6b7436f028.jpg",
   "https://telegra.ph/file/79c57327a446cdab22d04.jpg",
   "https://telegra.ph/file/eeaa074c2a67b0ea4a0b1.jpg",
   "https://telegra.ph/file/bf774d7166e4a991964cd.jpg",
   "https://telegra.ph/file/2bbdc0adf373285d08da3.jpg",
   "https://telegra.ph/file/723818b05dca43af39bcc.jpg",
   "https://telegra.ph/file/c37912e48bd93352f86d0.jpg",
   "https://telegra.ph/file/5dc28e1b9684afbcb0127.jpg",
   "https://telegra.ph/file/eeff500bebef2c9d0ff13.jpg",
   "https://telegra.ph/file/cf77d2cdcb0a6bc421fe2.jpg",
   "https://telegra.ph/file/a5751563a00d211cdd058.jpg",
   "https://telegra.ph/file/2fc1093f33434e760930b.jpg",
   "https://telegra.ph/file/e1131c0eddc584a9a943a.jpg",
   "https://telegra.ph/file/25e6f3c43f105b2bb871a.jpg",
   "https://telegra.ph/file/95a81db1c04a5964396ea.jpg",
   "https://telegra.ph/file/6f863138052eae15e8f7f.jpg",
   "https://telegra.ph/file/c2c73884b19f92faa2935.jpg",
   "https://telegra.ph/file/3ae47a98857a777ab7c41.jpg",
   "https://telegra.ph/file/e8b2f509ed6ab8f60e057.jpg",
   "https://telegra.ph/file/b92f2d7e1fbacaca21fa0.jpg",
   "https://telegra.ph/file/eb9606d26eea3a8383a26.jpg",
   "https://telegra.ph/file/5300b97af917fa86dbe08.jpg",
   "https://telegra.ph/file/6c7145506e09dae069bc3.jpg",
   "https://telegra.ph/file/273ef9a8c5f955a2fc16f.jpg",
   "https://telegra.ph/file/4971db4b1701be3a4a361.jpg",
   "https://telegra.ph/file/b937cd5e4593c1af9cfbc.jpg",
   "https://telegra.ph/file/8a1055e0b59ecfc1855fd.jpg",
   "https://telegra.ph/file/bae47fe2c81a48e6713df.jpg",
   "https://telegra.ph/file/a3270791f86df2d0e2415.jpg",
   "https://telegra.ph/file/1dca1f95a0ba7aa6bfa5d.jpg",
   "https://telegra.ph/file/681a80025847873dc7048.jpg",
   "https://telegra.ph/file/dcd876dd6561c1834abec.jpg",
   "https://telegra.ph/file/ca716acc08abe34fc8310.jpg",
   "https://telegra.ph/file/fb8a25e411d2e29e083ab.jpg",
   "https://telegra.ph/file/c48a28028d6b5cff09dd6.jpg",
   "https://telegra.ph/file/bbe5a2df399b09a52b4e0.jpg",
   "https://telegra.ph/file/1908f62846d6c72ba3742.jpg",
   "https://telegra.ph/file/8b776c3abdd4ee7f4578a.jpg",
   "https://telegra.ph/file/7654c5dbbd9bdee14881b.jpg",
   "https://telegra.ph/file/bb07b7d0943a1a36f38b8.jpg",
   "https://telegra.ph/file/20c11275a9f4743528255.jpg"
)




@Client.on_message(filters.command(["MEME"]))
def animequotes(_, message):
      message.reply_photo(random.choice(MEME_IMG))


@Client.on_message(filters.command("dare"))
async def dare(_, m):
         reply = m.reply_to_message
         if reply:
               api = requests.get("https://api.truthordarebot.xyz/v1/dare").json()
               text = api["question"]
               dare = f"""
**ʜᴇʏ! {reply.from_user.mention}
{m.from_user.mention} ɢɪᴠᴇ ʏᴏᴜʀ ᴀ ᴅᴀʀᴇ !
ᴅᴀʀᴇ**: `{text}`
               """
               await m.reply_text(dare)
         else:
               api = requests.get("https://api.truthordarebot.xyz/v1/dare").json()
               text = api["question"]
               dare = f"""
 **ʜᴇʏ! {m.from_user.mention} ʏᴏᴜʀ ᴅᴀʀᴇ ʜᴇʀᴇ !
 ᴅᴀʀᴇ**: `{text}`
               """
               await m.reply_text(dare)
               

@Client.on_message(filters.command("truth"))
async def truth(_, m):
         reply = m.reply_to_message
         if reply:
               api = requests.get("https://api.truthordarebot.xyz/v1/truth").json()
               text = api["question"]
               truth = f"""
 **ʜᴇʏ! {reply.from_user.mention}
  {m.from_user.mention} ɢɪᴠᴇ ʏᴏᴜ ᴀ ᴛʀᴜᴛʜ !
  ᴛʀᴜᴛʜ**: `{text}`
               """
               await m.reply_text(truth)
         else:
               api = requests.get("https://api.truthordarebot.xyz/v1/Truth").json()
               text = api["question"]
               truth = f"""
    **ʜᴇʏ! {m.from_user.mention} ʏᴏᴜʀ ᴛʀᴜᴛʜ ʜᴇʀᴇ !
    ᴛʀᴜᴛʜ**: `{text}`
               """
               await m.reply_text(truth)
               
# --------------------------------------------------------------------------------- #

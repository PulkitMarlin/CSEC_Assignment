# Task 3

In this task we were given a Audio with a secret in it. I couldn't help but I read the Update-1 before playing the audio, and that hint gave it away - 
as soon as I playd the Audio, I realized it consisted of only 2 statements being played again and again. 
Thus, I concluded that some binary message was hidden in this Audio, with both the statements correspondg to 0 and 1.

I tried looking for some software online which could generate subtitles for the audio, and I could use a python script to read the subtitles and map it to 0 and 1.
But, I was not able to find something which correctly translated the audio in the first 10 mins, so I thought of doing it manually as the audio was only around 3 mins long.

It was easy as the statement "Never gonna give you one" ended with a 1 so I mapped it to 1 and the other one to 0.
I got the string: 110100011101010110010000110001011011110101111101101001001101010101111101101110001100010110001100110011.

I tried breaking it into chunks of length 8 to convert it into an ASCII character, but the last chunk had only length 6, so I added 2 zeros to it. 
Then I tried to convert it to ASCII but it was gibberish. 
My first thought was that I took the opposite mapping of 1 and 0, so exchanged both of them. Still the output was gibberish.

I was confused and was looking for some visual pattern in the Binary String but couldn't find anything. 
I though about big-endian and little-endian, but realized that it changes the position of individual bytes, not inside a byte.

I thought of reading the question again, and that's when I saw the Update-2. 
I followed the same procedure as above for the Audio file given in Task-2 to obtain the String: 
00110100011101010110010000110001011011110101111101101001001101010101111101101110001100010110001100110011.

This time, it was exactly split into chunks of length 8 with no remainder. So I tried converting it to ASCII and it worked.
I got the flag - **4ud1o_i5_n1c3**

I was still curious that how is the same message hidden in the original file. 
So I decided to compare the 2 binary Strings and voila! The string from Update-2 had just 2 extra zeros in the beginning as compared to the original one. 
I was adding 0 to the last chunk, but it had to be added to the first chunk. This did not occur to me, and now that I know it, it can come handy sometime later!

**The final flag:**

4ud1o_i5_n1c3

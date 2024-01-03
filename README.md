# Hide-Secret-Text-In-a-Message (ZeroWidth_Steganography_API_Handler)
Hide Secret Text In a Message

## How the program works

When the program runs you'll be presented with the following output:

 ```
Encode or Decode:
 ```

Here you can either write `encode` or `e` to encode a message. Or you could write `decode` or `d` to decode a message.

### How to Encode:

Select the `encode` option:

```
Encode or Decode: encode
```

You'll then be propted to firstly enter your hidden message:

```
Enter hidden phrase: THIS IS MY HIDDEN MESSAGE
```

Following this you'll be prompted to fill in the public message, this is the message that everyone will be able to see.

```
Enter public phrase: THIS IS MY PUBLIC MESSAGE
```

Once you've entered the public phrase, press ENTER. You will then recieved the encoded text that contains the hidden message.
 
``` 
Here is your encrypted message:
###############################

THIS IS MY PUBLIC MESSAGE

###############################
Encode or Decode: 
```

### How to Decode:
 
Select the `decode` option:

```
Encode or Decode: decode
```

You'll then be propted to enter a phrase to decode: 

```
Enter phrase to decode: THIS IS MY PUBLIC MESSAGE
```

You will then recive your decoded message:

```
Here is your decrypted message:
###############################

THIS IS MY HIDDEN MESSAGE

###############################
Encode or Decode: 
```

Go to this link to use the website: https://neatnik.net/steganographr/


For developers. The following link will take you to the api page. https://neatnik.net/steganographr/api/



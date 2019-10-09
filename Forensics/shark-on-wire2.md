# Problem

Find the flag in this pcap file

# Solution

There's a number of false flags in here, combined with a bunch of junk data. So, let's look for something interesting....

Open the "Conversations" window in the Statistics menu and look for anything interesting. There are
some connections that look at look like SSH, so they're easy to overlook. However, they are very short
and use UDP. That's suspicious. When examining the data, the packets all look the same with a few repeated "a" characters. The only thing that changes is the source port.

At first, I noticed that the checksum in the packet was changing, and realized that was because of the source port. On a whim, I noticed that the source ports were all in the 5xxx range with xxx because within the range of the ascii table. So, I decided to check the first packet (source port 5112) in the sequence:

```
5112 - 5000 = 112 = 'p'
```

Interesting. Let's do the next few source port numbers to see if it was just coincidence...

```
5105 - 5000 = 105 = 'i'
5099 - 5000 = 099 = 'c'
5111 - 5000 = 111 = 'o'
5067 - 5000 = 067 = 'C'
5084 - 5000 = 084 = 'T'
5070 - 5000 - 070 = 'F'
```

Coincedence? Doesn't look like it. Let's finish the entire 22/udp packet sequence:

**Flag: picoCTF{p1llf3r3d_data_v1a_st3g0}**

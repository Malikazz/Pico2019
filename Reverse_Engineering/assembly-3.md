# asm-3

## test.S

```
asm3:
        <+0>:   push   ebp
        <+1>:   mov    ebp,esp
        <+3>:   xor    eax,eax
        <+5>:   mov    ah,BYTE PTR [ebp+0xb]
        <+8>:   shl    ax,0x10
        <+12>:  sub    al,BYTE PTR [ebp+0xd]
        <+15>:  add    ah,BYTE PTR [ebp+0xe]
        <+18>:  xor    ax,WORD PTR [ebp+0x12]
        <+22>:  nop
        <+23>:  pop    ebp
        <+24>:  ret
```

## Problem

What does asm3(0xdff83990,0xeeff29ae,0xfa706498) return? Submit the flag as a hexadecimal value (starting with '0x')

## Solution

### Logical Stack layout

```
    +---------------+
    | old ebp       | <-- ebp
    +---------------+
    | ret           | <-- ebp + 0x4
    +---------------+
    | 0xdff83990    | <-- ebp + 0x8 (arg1)
    +---------------+
    | 0xeeff29ae    | <-- ebp + 0xc (arg2)
    +---------------+
    | 0xfa706498    | <-- ebp + 0x10 (arg3)
    +---------------+
```

### Actual Stack Layout (in groupings, due to endian-ness)

```
Byte grouping:

    +0x8 +0x9 +0xA +0xB +0xC +0xD +0xE +0xF +0x10 0x11 0x12 0x13
    +----+----+----+----+----+----+----+----+----+----+----+----+
    | 90 | 39 | f8 | df | ae | 29 | ff | ee | 98 | 64 | 70 | fa |
    +----+----+----+----+----+----+----+----+----+----+----+----+

Word grouping:

    +0x8   +0xA   +0xC   +0xE   +0x10  +0x12
    +------+------+------+------+------+------+
    | 3990 | dff8 | 29ae | eeff | 6498 | fa70 |
    +------+------+------+------+------+------+
```

### Code Walkthrough

```
asm3:
        <+0>:   push   ebp
        <+1>:   mov    ebp,esp
        <+3>:   xor    eax,eax                  ; eax = eax ^ eax = 0
        <+5>:   mov    ah,BYTE PTR [ebp+0xb]    ; ah = 0xdf (ax = 0xdf00)
        <+8>:   shl    ax,0x10                  ; ax = ax << 2 = 0x0000
        <+12>:  sub    al,BYTE PTR [ebp+0xd]    ; al = 0 - 0x29 = 0xd7 (ax = 0x00d7)
        <+15>:  add    ah,BYTE PTR [ebp+0xe]    ; ah = 0xff (ax = 0xffd7)
        <+18>:  xor    ax,WORD PTR [ebp+0x12]   ; ax = ax ^ fa70 = 0x05a7
        <+22>:  nop
        <+23>:  pop    ebp
        <+24>:  ret
```

eax = 0x5a7

**flag: picoctf{0x5a7}**

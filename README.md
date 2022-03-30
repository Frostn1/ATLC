# ATLC
Animation Tooling Library for C made using a special formatting file
( Pronounced as Atlas )

## File format
Using .atl files we can create our own animation file, inorder to create ascii styles and movements.

---

### The atl header
Every .atl file includes a header at the start of the file, which gives us meta data aboutr the file itself.<br>
The header can be visually abstracted as this `C` struct :<br>
```c
struct atl_header {
    char magic[3]; // `ATL`, lets us know we got the right file infront of us
    uint32_t frames; // Number of frames in our file
    uint8_t colormode; // Lets us know the color moode ( i.e. amount of bits per color the animation uses )

};
```

As we don't know the size of the file we are about to parse, but the number of frames we need to parse ( more on frames later on ), we can parse the entire file by counting the number of frames we have read so far.<br>

As each frame is read and proccessed, its executed by the library code ( aka `WhiteMarker` ), and used to display the animation on your screen<br>

---

### Frames
As we said before our entire atl file is cut into different frames, which each one has a header, and a tail ( i.e. a structure which lets us know we have ended parsing the current frame).<br>
Each frame is used to display some kind of animation on the screen, and cutting the animation into frames lets us part the animation into different main parts, and see more clearly how it works.<br>
`Note : The entire file can be built up using one frame, but we will soon find out this is a bad habit, as framing up the animation lets us pick and choose theh frames we want to keep`<br>

Frames, as the file itself, also have their own header,
which can be visually abstracted using `C` structs system, as follows :<br>

```c
struct frame_header {
    uint16_t frame_index; // Lets us know the index of the current frame, marked with the file creator
    uint16_t default_tick; // Default time delay
    int16_t tick_mult; // 10 expoonent multiplier for delay conversion
};
```

As we can already see the `frame_header` has to unique fields which capture the time between opcodes execution in each frames, which relate to each other in some way.<br>
<b>default_tick</b> - Default time between each opcode execution in the frame, noted in nano seconds.<br>
<b>tick_mult</b> - As showing a second using nano seconds, will make a very large number, we can use a 10 expoonent multiplier to make this simpler, and more memory conservative.
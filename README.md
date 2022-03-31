# ATLC
Animation Tooling Library for C made using a special formatting file
( Pronounced as Atlas )

## File format
Using .atl files we can create our own animation file, inorder to create ascii styles and movements.<br>

As each frame is read and proccessed, its executed by the library code ( aka `WhiteMarker` ), and used to display the animation on your screen<br>

---

### The atl header
Every .atl file includes a header at the start of the file, which gives us meta data about the file itself.<br>

As we don't know the size of the file we are about to parse, but the number of frames we need to parse ( more on frames later on ), we can parse the entire file by counting the number of frames we have read so far.<br>

The header can be visually abstracted as this `C` struct :<br>
```c
struct atl_header {
    char magic[3]; // `ATL`, lets us know we got the right file infront of us
    uint8_t atl_mode; // Current atl mode the file is in
    uint32_t frames_count; // Number of frames in our file
    uintxx_t index_table[]; // Frames indices
    uint8_t colormode; // Lets us know the color moode ( i.e. amount of bits per color the animation uses )
    uint64_t overflow_count; // Number of frames the overdue max frame size
    uint64_t overflow_table[]; // Frames indices which overflow the max frame size
    
};
```
><b>index_table</b> - Table which is used to captrue the indices of all of the frames in the file, relative to the start of the file.<br>
Each item in the array will be relatiive in size to the atl mode the file is in.<br><br>So in ATL-8 mode, each item in the array ( i.e. index_table ), can be represented with the `C` size of <font color="#0081cd"><i>uint8_t</i></font>.

><b>overflow_table</b> - Frames index that overdue the max size limit for each frame ( dictated by the atl mode ), the index is relative to the start of the file.<br><br>
The size of the `overflow_table` field will be relative to the `overflow_count` field, which will count the number of frames that have overflowed in the current file, and not all of the frames ( This is different from how the `index_table` works).<br><br>This means it will be more memory efficient, when no frame overflowed, no memory will be used

><b>atl_mode</b> - Dictates the mode ( i.e. frame size ) the file is limited at.<br><br>
[ <i>ATL-8</i> ] : mode where every frame size can be represented with an 8 bit unsigned number.<br>
[ <i>ATL-16</i> ] : mode where every frame size can be represented with an 16 bit unsigned number.<br>
[ <i>ATL-32</i> ] : mode where every frame size can be represented with an 32 bit unsigned number.<br>
[ <i>ATL-64</i> ] : mode where every frame size can be represented with an 64 bit unsigned number.<br>



---

### Frames
As we said before our entire atl file is cut into different frames, which each one has a header, and a tail ( i.e. a structure which lets us know we have ended parsing the current frame).<br>
Each frame is used to display some kind of animation on the screen, and cutting the animation into frames lets us part the animation into different main parts, and see more clearly how it works.<br>
`Note : The entire file can be built up using one frame, but we will soon find out this is a bad habit, as framing up the animation lets us pick and choose theh frames we want to keep`<br>

Frames, as the file itself, also have their own header,
which can be visually abstracted using `C` structs system, as follows :<br>

```c
struct frame_header {
    
    uint16_t frame_index; // Lets us know the index of the 
    current frame, marked with the file creator
    uint64_t size; // Size of the current frame
    uint16_t default_tick; // Default time delay
    int16_t tick_mult; // 10 expoonent multiplier for delay conversion+
};
```

As we can already see the `frame_header` has to unique fields which capture the time between opcodes execution in each frames, which relate to each other in some way.<br>

><b>default_tick</b> - Default time between each opcode execution in the frame, noted in nano seconds.<br>

><b>tick_mult</b> - As showing a second using nano seconds, will make a very large number, we can use a 10 expoonent multiplier to make this simpler, and more memory conservative.

---

### Opcodes
Every frame in the .atl file is constructed from different kind of opcodes, which are a single known size, and represent some sort of action that is to be made to the text on screen.<br>
Some of thses actions can include moving of the cursor, erase, changing of color, writing of letter and more.<br><br>
Each opcode will start with a ssid the size of `uint8_t` which will represent the type of opcode we are about to parser, all opcodes will have this field. This lets us differentiate between the different opcodes available.<br>

`Note : List of all the available opcodes can be seen at the end of the Opcodes part`

An example code for an opcode, could be written like this ( This is the opcode for cleaning the screen ) :

```c
struct atl_op_cls {
    uint8_t ssid; // Unique id
    uint8_t reset; // Reset cursor pos to 0,0
};
```


<details>
  <summary><b>Full List of Opcodes</b></summary>
    <ol type = "1">
    <li>
        <details><summary>Clear Screen</summary>
        The clears screen opcode, does as what its name suggests.<br>
        Its structure in code can be represented using c strucures this way :<br>
        ```c
        struct atl_op_cls {
        }```
    </li>
  </ol>
  </details>
</details>



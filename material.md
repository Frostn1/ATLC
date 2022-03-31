```c
/** returns next frame header to process or NULL */
atl_frame_header_t *read_frame(void *data, size_t current_offset, atl_header_t *ahdr, atl_frame_header_t *hdr)
{
  static int frame_count = 0;
  static int lookup_count = 0;
  frame_count += 1;
  ...
  atl_frame_header_t *next;
  if(hdr->size == 0)
  {
    if(lookup_count >= ahdr->offset_count) next = NULL;
    else next = &data[ahdr->offsets[lookup_count++]];
  }
  else
  {
    next = &data[current_offset];
  }
  ...
  if(frame_count >= ahdr->frame_count) next = NULL;
  return next;
}
```



# Ideas
- overflow table
Used to capture the indices of frames that ovverdue the size limit in theh current atl mode
- atl modes
atl-8 ( 8 bits per frame index), atl-16 ...
dictates the maximum size of each frame that is allowed in  the file
- index table
Table which is used to captrue the indices of all of the frames in the file, relative to the start of the file


inroder to calculate the current header using the index table
`(frame_header*)(&file_memory[sum(header.offsets, header.offsets + 3)])` uses that every index is relative to the one before it.<br>
or<br>
`(frame_header*)(&file_memory[header.offsets[3]])` uses the every index is relative to the start of the]| file.<br>



```
the impl scans index_table from left to right, it keeps track of how many values overflowed
so once it reaches frame 4, it knows that no values overflowed before so it looks up index 0 in the overflow_table
...
when you scan, you know at what index the next overflowed value is
```

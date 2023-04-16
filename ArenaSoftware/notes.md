/*
** Robot Combat Arena Control Code
** Using Ardunio framework / ESP32 (maybe STM32 with GPIO changes)
** Read 8 buttons
** ready and tap out for 2 teams
** Match start / pause / end /reset for ref
** Serial out to hacked iCruze display boards
** Will control 1 or 2 "stoplight" towers with signal horns
** NF 2022/06/04

*/

// State diagram
/* no match states:
    Reset and ready for start ( solid yellow )
      team a ready
      team b ready
      both teams ready (blinking yellow)
    match pause (blinking yellow or blinking red / match timer paused)
    match tapout (blinking red)
    match end by KO (blinking red)
    match end by time (solid red)
  Match states
    Start pressed (3 secs of blinking yellow followed by green.  Match timer starts then)
    start pressed after pause (same as above with timer resuming)
    active match (solid green)
    10 sec count down (blinking green)
  Horn will sound at match end, time up or team tapout
*/
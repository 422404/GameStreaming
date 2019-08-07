package input

// #cgo LDFLAGS: -lX11 -lXtst
// #include <X11/extensions/XTest.h>
import "C"

// KeyDown emulates a key press on the current display
func KeyDown(character string) {
	var display *C.Display
	var c C.uchar

	if character[0] >= 0x20 {
		display = C.XOpenDisplay(nil)
		c = C.XKeysymToKeycode(display, C.ulong(character[0]))
		C.XTestFakeKeyEvent(display, C.uint(c), 1, C.CurrentTime)
		C.XCloseDisplay(display)
	}
}

// KeyUp emulates a key release on the current display
func KeyUp(character string) {
	var display *C.Display
	var c C.uchar

	if character[0] >= 0x20 {
		display = C.XOpenDisplay(nil)
		c = C.XKeysymToKeycode(display, C.ulong(character[0]))
		C.XTestFakeKeyEvent(display, C.uint(c), 0, C.CurrentTime)
		C.XCloseDisplay(display)
	}
}

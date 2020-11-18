module vuipy

import ui
import os

import gg


const (
	win_width  = 400
	win_height = 200
)

struct App {
mut:
	counter string = '0'
	window  &ui.Window = 0
}


pub fn app() &App{
	mut app := &App{}
	app.window = ui.window({
		width: win_width
		height: win_height
		title: 'vuipy'
		state: app
	},[])

	//for item in widgets{
	//	app.window.children << item
	//}
	//}, [
	//	ui.label({
	//		text: "hello"
	//	}),
	//])

	return app
}

pub fn run(mut app App){
	ui.run(app.window)
 	set_title(mut app)
}

pub fn add_widget(mut app App, widget ui.Widget){
	println("add_widget!! by Vlang")
	app.window.children << widget
}

pub fn label(text string) &ui.Label{
	println("vlang label $text")
	label := ui.label({
		text:"heyy"
	})
	return label
}


pub fn set_title(mut app App){
	app.window.set_title("unkoooo")
}


fn btn_count_click(mut app App, btn &ui.Button) {
	app.counter = (app.counter.int() + 1).str()
    println("clicked! $app.counter")
}

import vuipy

fn main(){
	mut app := vuipy.app()
	vuipy.add_widget(mut app, vuipy.label("hello"))
	vuipy.run(mut app)
}

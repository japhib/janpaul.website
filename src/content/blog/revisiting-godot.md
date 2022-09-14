---
title: "Revisiting Godot: GDScript"
subtitle: "So far, this blog has exclusively been about game engines. Why stop now?"
date: 2022-09-14T10:05:48-06:00
draft: false
---

[Godot](https://godotengine.org/) (pronounced "guh-DOE") is a [fully open-source](https://github.com/godotengine/godot) game engine that aims to compete with giants like Unity and Unreal. I've written about it [in the past](/blog/ultimate-game-engine/), and at that time I was pretty harsh:

> GDScript is terrible. I refuse to use a language that I will only ever use for this one particular program. They do have C# support through Mono, which is cool. And it does have some other nice features, like first-class 2d support (including 2d lighting!). However, most of the rest of the engine feels pretty bad, and when I’m using it, I can’t help but think, “this is just a crappier version of Unity!”

However, when I wrote that, I had only played with Godot a tiny bit. Since then, I've fiddled around with it a bit more, and I have to admit that it's a lot nicer than I gave it credit for.

# GDScript

GDScript is the main scripting language that Godot supports. GDScript is a Python-like language, with some [Godot-specific innovations](https://docs.godotengine.org/en/stable/about/faq.html#what-is-gdscript-and-why-should-i-use-it):

1. **Threading support** (a rarity in dynamic scripting languages such as Python and Lua)
2. Simple and straightforward **C++ bindings**, including the ability to **extend C++ classes** - object-orientation is a staple of Godot's architecture
3. **Native, value-based vector types** (Vector3, Matrix4). Typical scripting languages like Lua, Python, and Javascript only support reference-based user classes, which generates a lot of garbage
4. Memory management using **reference counting** rather than garbage collection, eliminating unpredictable GC pauses
5. Tight IDE integration - Godot has an **embedded GDScript code editor**, providing in-editor docs, code completion (for _your project's_ assets!), live editing, and other tools

In my [other blog post](/blog/ultimate-game-engine/) I _specifically_ lamented the lack of value types in languages such as Java, Javascript, and Lua. GDScript directly fixes that flaw.

Another rant I had in that blog post was that in Unity, "you're not coding, you're 'scripting'." Godot actually leans into this with GDScript by making the scripting language itself very lightweight, and tightly integrated with the engine. IMO this is a better solution. It's easy and fast to make a new GDScript script -- you don't even have to wait for it to compile! Plus, it makes it very clear that you're not using regular C#, you're using a language specific to this game engine.

There are some situations where I still wouldn't use GDScript. For example, if I were to make a game like [Barnard's Star](https://pollywog.games/barnards-star.html) where I needed to run the game logic on a server outside of the game engine, I'd use C# instead. I don't believe there's any way to run GDScript outside of Godot Engine itself.

To sum up, when I actually gave GDScript a chance, it quickly became clear that it's a well-thought-out language that solves a lot of problems.

# Godot: the future???

Godot is far from perfect, but I love that it's open source. Unity has served us well enough, but with all its warts, I'd love to try something else out for a change. My current project, Barnard's Star, is much too far gone to switch engines at this point -- I've got 20k lines of Unity-specific C#, and another 30k+ lines of game logic C#. But next time I start a new project, I'd love to start it on Godot!
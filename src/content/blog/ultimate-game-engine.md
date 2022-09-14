---
title: The quest for the Ultimate Game Engine
subtitle: "(or: why they all *suck*)"
date: 2021-06-03T12:00:00-06:00
draft: false
---

I've been using Unity for about 4 years now. I've even used it to develop [a couple of commercial projects](https://pollywog.games). So obviously, it can get the job done. It has a [huge](https://www.reddit.com/r/Unity3D/) [community](https://forum.unity.com) and there are tons of [high-quality](https://catlikecoding.com/unity/tutorials/) [tutorials](https://www.youtube.com/user/Brackeys) online. It appears to be the [most-used game engine](https://itch.io/game-development/engines/most-projects) among indies and hobbyists. And best of all, it's free.

... so what's my gripe with it?

A lot of things, really. Here the major ones, in no particular order. 

**_Disclaimer:_** _All my complaints are specific to me, with my particular (coding-heavy) background. I know these points really aren't applicable to every game developer. I'm just speaking for myself here._

### It's editor-centric

Unity has a lot of features intended so that people *other* than coders can participate in the game development process. That's great and all, but I'm a coder. When I want a reference to an object on another object's script, I don't want to have to switch from the IDE to the Unity editor, wait a solid 5 seconds for my latest changes to compile, find and select the object I'm working on, hunt around for the object I want to connect to it, and then use my *mouse* to *physically* drag & drop the dependency over. Can you imagine anything more primitive?

And that's just one example. There are a million little things that would be awesome if you could do either in code or in editing a text file for settings, but you just can't. You *have* to use the editor. There's no way around it.

### It's 3d-centric

You can have a 2d game in Unity, but you never really feel like Unity is _meant_ to be used for it.

For example: to create a sprite in a scene, you drag an image into the scene view. It appears wherever you dropped it in the scene view. However, when you look in game view, it doesn't show up! What's wrong? The answer is usually that when you drag & dropped it into the scene, Unity put the X and Y coordinates of that object where you expected, but the Z coordinate is at something ridiculous like -2548.19. And because the game camera is at a Z position of -10, it can't see that object. The fix is, of course, just to change the Z coordinate back to 0, where it belongs in a 2d game. This seems like it'd be a simple fix for Unity to make, but of course they won't do it because it's only for 2d.

Another example is the striking lack of support for a good 2d lighting system. Unity only _very_ recently [added support](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@12.0/manual/Lights-2D-intro.html) for this, but it has terrible performance unless you're on a high-end graphics card, and it's only available on the Universal Render Pipeline, which comes with its own set of issues. This is in spite of [every](https://www.hollowknight.com) [major](http://www.celestegame.com) [indie](https://store.steampowered.com/app/105600/Terraria/) [2d](https://store.steampowered.com/app/294100/RimWorld/) [game](https://store.steampowered.com/app/588650/Dead_Cells/) from the [past](https://store.steampowered.com/app/262060/Darkest_Dungeon/) [several](https://store.steampowered.com/app/311690/Enter_the_Gungeon/) [years](https://store.steampowered.com/app/860950/Mark_of_the_Ninja_Remastered/) utilizing a 2d lighting system. I guess they just ... I don't know, saw that everyone was somehow managing to implement it on their own, and figured it wasn't that important?

There are, of course, workarounds for this. But the more time you spend on workarounds, the less time you can spend on making cool content for your game.

> **Edit August 2022:** On the topic of Unity's 2d lighting in URP, I feel like I have to mention that Barnard's Star has been released, and it uses Unity's 2d lighting system, as well as the URP. Performance is okay, although I had to disable all shadow casters and only use one sorting layer.
>
> In the future, if I were to write a game that was heavily dependent on a lot of 2d lights with lots of shadow casters, I'd go with a framework like MonoGame where I have more control over rendering.

### You're not coding, you're "scripting"

In Unity, you don't have access to the actual program that is running (the engine code). You only have access to scripts on objects. So if you want an arbitrary piece of code to run in a scene, you have to create a new GameObject in the scene you want and add your script to it. Oh, what's that? You want your code to run in _every_ scene? Or maybe _before_ the scene is loaded? Or pass data _between_ scenes? Sorry, you can do that but it's always going to feel like weird, hacky workarounds and there are a ton of edge cases you're going to have to deal with. Have fun :)

You don't have full control over the program, how it runs, or how it's structured. You're just going to have to deal with it if you want to use Unity.

----

So. The obvious question is now, **why not just use a different engine?** This, of course, led to my **Quest for the Ultimate Game Engine,** which I have been on for the past year or two, on and off.

# The other game engines

The answer is that all the other game engines suck just a little more. Let's go through them, shall we?

- **Unreal**

Unreal Engine is completely 3d based. Also, it uses C++ which feels really ... primitive. I get that it's better for performance, and it's better for consoles, but as an indie developer I care more about the speed of iteration. And when I have to write a function signature in two separate files, and I'll get a compiler error if they don't match, I lose the will to continue reeeaal quick.

- **Godot**

GDScript is terrible. I refuse to use a language that I will only ever use for this one particular program. They do have C# support through Mono, which is cool. And it does have some other nice features, like first-class 2d support ([including 2d lighting!](https://docs.godotengine.org/en/stable/tutorials/2d/2d_lights_and_shadows.html)). However, most of the rest of the engine feels pretty bad, and when I'm using it, I can't help but think, "this is just a crappier version of Unity!"

Nothing against Godot as a project. I love that it's open source, and I hope they go a long ways. I just think that it's similar enough to Unity that it doesn't really solve my problems. It's quite editor-centric, everything is "scripting" rather than coding (maybe even more so than Unity), and it all feels more buggy and janky than Unity does, simply because it's open source rather than a big commercial project.

> **Edit August 2022:** I've actually played with GDScript a fair amount since writing this post and I've changed my mind about it. I think that as long as you're scripting the engine, rather than writing code from scratch, it's actually really nice. It has a level of integration with the editor that is impossible if you're using an existing programming language.
>
> In short, I've started to understand [some of the reasons](https://docs.godotengine.org/en/stable/about/faq.html#what-is-gdscript-and-why-should-i-use-it) the creators of Godot give for making a new scripting language.
>
> **Added September 2022:** Made a whole blog post with [my thoughts about GDScript](/blog/revisiting-godot/).

- **GameMaker Studio**

From the outside, GMS seems really nice. Some really impressive 2d games have been made using it -- [Hyper Light Drifter](https://store.steampowered.com/app/257850/Hyper_Light_Drifter/), [Nuclear Throne](https://store.steampowered.com/app/242680/Nuclear_Throne/), and basically every other game from Vlambeer's catalog. And I actually did buy a 1-year copy of GMS on sale a few months back, so I've been trying it out. But I have to say that it feels like a step in the wrong direction. It has drag & drop coding and a built-in sprite editor, which are both features intended very much for non-coders. Safe to say it is _highly_ editor-centric. Not to mention that GameMaker Language is terrible. I repeat:

> I refuse to use a language that I will only ever use for this one particular program.

GML is actually worse than GDScript in a lot of ways. No inheritance, or functional programming, or even objects. This is my third point, "you're not coding, you're 'scripting'" turned all the way up to 11. No thank you.

### The frameworks

Game frameworks typically give you a lot more control over what you're creating, at the cost of not having an editor and having less tooling surrounding the process. I've tried several of them:

- **[Love2d](https://love2d.org)**

Love2d or LÖVE is pretty cool. It's nice for prototyping things. However, Lua gets _really_ old for projects that last longer than a weekend. It's a fully dynamic language, which means:

- You can only catch errors at runtime
- Refactoring is a huge pain
- No types, so it's hard to have IDE support like autocomplete -- so any time you want to call a function, you're most likely going to have to look up the exact number and order of parameters, as well as the return value

Lua also has some other weird quirks. For example, array indices start at 1, the syntax seems extra verbose (you end up typing the words `function` and `end` a LOT), and for some reason there's no `+=` operator.

- **[LibGDX](https://libgdx.com)**

On paper, LibGDX is a match made in heaven. It's similar to Love2D in that it's only a framework, not a game engine, so I'm free to implement my own render pipeline exactly as I see fit. However, Java is obnoxiously verbose, and is missing a lot of the functionality of a more "modern" language like C#. Coroutines, stack-allocated structs, the `var` keyword, async/await, non-terrible interop with C/C++, it's all missing from Java.

Kotlin is slightly better. But there's only so much they can do with a language that runs on the JVM. For instance, stack-allocated structs or multiple return values will simply never be supported because that's not a part of the JVM. And when you want to avoid allocating every frame for performance reasons, this results in some obnoxious, non-idiomatic coding practices. Kotlin also doesn't have HTML5 support at the moment. I assume that'll be remedied eventually, but for now it's just yet another turnoff for me from LibGDX.

- **[Monogame](https://www.monogame.net)/[FNA](https://fna-xna.github.io)**

Monogame and FNA are both re-implementations of the [Microsoft XNA](https://en.wikipedia.org/wiki/Microsoft_XNA) game libraries. Of this list, they seem the most promising to me. I have yet to _really_ dig into them, though I have tried to use Monogame and it has a few issues.

The biggest issue to me is the lack of HTML5 export. I like to sometimes make small games and throw them up on [itch.io](https://itch.io). When you see a game on there and you have to download it, then get past all the obstacles your computer's OS tries to throw in front of you (Don't open this! It's malware! Are you sure you want to open it? Please go through one more extra step to open this just so you _really_ know this is dangerous) it's a turn-off at best.

The other thing stems from the fact that both of these are re-implementations of older, proprietary, discontinued software -- using the APIs just _feels_ off. For example, in order to load assets into your Monogame project, you have to "build" them using the "Monogame Content Builder." It's a standalone app where you just click your files and say "yes, I want these in my project." Oh and by the way, the standalone app [doesn't work at all on mac](https://github.com/MonoGame/MonoGame/issues/7513) at the moment. Since Mac is my main development environment, this is another big turnoff.

- **[Haxe](https://haxe.org)**

Haxe is interesting to me. It's not _really_ its own programming language -- you're effectively coding for 5 different platforms at once, using a fairly leaky abstraction. It's flexible -- it has preprocessor defines if you want platform-specific behavior -- but it just [never took off](https://trends.google.com/trends/explore?date=all&geo=US&q=%2Fm%2F0dbjtf,%2Fm%2F0dsbpg6). It seems like the main group of people using Haxe are people who were really into ActionScript 3 (the langauge that was used for coding in Flash) and were able to make a smooth transition over to OpenFL. There are some other frameworks that seem alright and even have a few devoted users, but I could never really get into it.

I think the main problem is just that the communities are all so small. This means that the tools aren't very mature, stuff breaks frequently, there aren't many tutorials, and if you get stuck it just isn't very easy to get help.

There are other issues too, though. Since it compiles to things like JS and the JVM, it has inherited a lot of the sloppy memory-management patterns of those platforms. Also, despite compiling to a dozen different languages, the actual process of integrating it with any native libraries in those languages remains mysterious and complicated. It kinda seems like in order to succeed with Haxe, you need to live in France and be buddies with [Nicolas Cannasse](https://github.com/ncannasse).

- **[Luxe](https://luxeengine.com)**

This honestly looks *amazing*. The only problem is ... it's not released yet. So I can't use it.

**Update, July 2021:** I got accepted into the Luxe closed beta! I'll make a post about it soon.

# Sounds like you just want to write your own game engine.

Yeah, I guess you're right.

I have toyed with this a bit, and even got decently far with writing my own C++ game framework. I ditched it after realizing (again) how terrible C++ is to work with, but at some point I would like to try again with something like Rust or C#.

That's so much *work* though. I just want to boot up a game engine that

- uses a modern programming language
- lets me allocate things on the stack
- recognizes all my assets without having to go through another tool
- exports to desktop (windows, mac, linux), mobile (iOS, android), and web (HTML5)
- has coroutines
- isn't editor-centric
- allows me to implement my own rendering pipeline without too much trouble

**Is that so much to ask???**
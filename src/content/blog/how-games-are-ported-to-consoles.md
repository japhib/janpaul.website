---
title: "Gaming consoles only support C++ -- How games in other languages are built"
date: 2022-09-29T19:09:07-06:00
draft: true
---

> Hi, I'm Jan, a full-time softwware developer for [Divvy](https://getdivvy.com/) and hobbyist game developer under [Pollywog Games](https://pollywog.games/). Thanks for reading!

## Wait, gaming consoles only support C++?? Why!??

When I was learning how to program for the first time, I was told the language I was using (Java) had a magical thing called a "Garbage Collector" (GC) that made manual memory management obsolete. Later on, using C++ I got a taste for what manual memory management feels like -- when you're not used to it, it's painful. My takeaway from this, which persisted all the way through college and several years afterwards, was that **C++ and other non-GC languages are obsolete languages that no one uses anymore.**

Why would you use a language that makes you take out your own trash when there are languages available that do it for you?

The answer to that question is **hard real-time requirements**. There's a [whole class of software applications](https://stackoverflow.com/a/30498130/530728) that can't stand to wait around at non-deterministic intervals, for random amounts of time, for the GC to pick up the trash. Mission-critical software for cars and airplanes, physical simulations, and many video games fit into that category. The garbage collector runs whenever it decides it needs to; you can't really control when it runs, or for how long it runs. As video games have traditionally been the 

### The closed garden of video game consoles

"Hard real-time requirements" is a big reason why people might use C++ _in general_; but there are is another big reason that is very specific to gaming consoles for why C++ is the only official language supported: **Gaming console APIs are closed-source and under NDA.**

If you want to develop a game for a gaming console, you have to sign up for a developer account and get approval from the company that makes the console. (i.e. Microsoft for Xbox, Sony for PlayStation, and Nintendo for the Switch.) As part of this process, you have to sign an NDA ([here's PlayStation's](https://www.sec.gov/Archives/edgar/data/946581/000162828017005833/ex10-48.htm)) that effectively **prohibits you from sharing with other developers stuff like the console's API details, or any console-specific code that you create.**

I'm not sure why this requirement exists. I guess it's a way for the console makers to protect their trade secrets, or maybe they're hoping for [security by obscurity](https://en.wikipedia.org/wiki/Security_through_obscurity). Whatever the motivation, the result is that **open-source projects for gaming consoles cannot exist.** This means that if you want to port a language to a console, you have to do it yourself, or at least with only your company -- that's a pretty big deterrent. Considering that most modern languages are either open source ([Rust](https://github.com/rust-lang/rust), [Go](https://github.com/golang/go), [Kotlin](https://github.com/JetBrains/kotlin)) or have open source implementations ([Java](https://github.com/corretto/corretto-11/), [C#](https://github.com/dotnet/core), [Javascript](https://chromium.googlesource.com/v8/v8.git)), it's not surprising that these languages don't make it onto a closed-source platform.

> Coincidentally, this is one of the big reasons why there's not a big, popular open-source game engine yet -- you have to register with the console maker as a company, which is something the community can't do. [Godot](https://godotengine.org/) is getting there, but has yet to achieve industry popularity. The maintainers of Godot have a page in their documentation dedicated to talking about this problem, [check it out!](https://docs.godotengine.org/en/stable/tutorials/platform/consoles.html)

----

With some background out of the way, let's go through popular game-making languages & platforms, and talk about how each one enables console development with languages other than C++.

## Unity - C#

Unity is the most popular game engine by far -- here are figures for [Steam](https://steamdb.info/tech/) and for [Itch.io](https://itch.io/game-development/engines/most-projects). While the core of the Unity engine is written in C++, all user scripts are written in C#.

Unity uses a proprietary tool called [IL2CPP](https://docs.unity3d.com/Manual/IL2CPP.html) to convert compiled C# IL ("Intermediate Language") into C++, which is then compiled into a native binary. Here's how it works, from the [Unity manual](https://docs.unity3d.com/Manual/IL2CPP.html#HowItWorks):

<blockquote>

When you start a build using IL2CPP, Unity automatically performs the following steps:

1. The Roslyn C# compiler compiles your application’s C# code and any required package code to .NET DLLs (managed assemblies).
2. Unity applies managed bytecode stripping. This step can significantly reduce the size of a built application.
3. The IL2CPP backend converts all managed assemblies into standard C++ code.
4. The C++ compiler compiles the generated C++ code and the runtime part of IL2CPP with a native platform compiler.
5. Unity creates either an executable file or a DLL, depending on the platform you target.

</blockquote>

According to [this Unity blogpost about IL2CPP](https://blog.unity.com/technology/an-introduction-to-ilcpp-internals), it was first shipped in 2015 and supported iOS 64-bit and WebGL, with other platforms coming quickly afterwards. 

This is a pretty novel approach, but as we'll see, converting other languages to C++ and then compiling normally is a pretty common strategy. The ahead-of-time nature of the compilation means that reflection is not really available in the same way as it is on regular JIT-ed platforms; this results in some hacky workarounds for things that normally rely on reflection, such as JSON serialization. [Here's one we had to do](https://github.com/jilleJr/Newtonsoft.Json-for-Unity/wiki/Fix-AOT-using-AotHelper) for my current project, [Barnard's Star](https://pollywog.games/barnards-star.html). The gist of it is that IL2CPP strips out any types that it thinks are unused, so sometimes you have to artificially add instantiations of types (especially generic ones) that in order for it to keep them around.


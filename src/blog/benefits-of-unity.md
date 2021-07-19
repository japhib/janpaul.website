--
title: The Benefits of Unity
description: the reasons it's so flippin' popular
date: July 19 2021
--
In my [last post](ultimate-game-engine.html), I detailed all the many reasons why I dislike Unity and find it frustrating to work with. Despite all those reasons, I've released [a commercial game](https://pollywog.games/card-crusade.html) built with Unity and am close to releasing [a second](https://store.steampowered.com/app/1217500/Barnards_Star/). That amounts to **several years** of working with Unity -- if I hate it so much, why haven't I bailed before now?

Well, the reason is that the benefits of using Unity outweigh the costs for me. I may or may not keep using it for future projects, but these are the reasons why it's been good enough for past and current projects. I've already gone into _excruciating_ detail on my gripes about the engine, so to be fair I need to talk about the benefits of it.

**_Note:_** _Like the last post, a lot of these benefits are specific to me and don't necessarily apply to other people, with a different background or different goals._

### The editor isn't that bad, and can actually be pretty nice for certain things

For better or worse, the Unity editor is a huge part of the development process. This was especially annoying at first, but after using Unity for a while, I've become quite comfortable in how to use it. So I don't think it's that bad anymore.

What's more, there are certain tasks that the editor actually does make quite a bit easier. For instance, **putting together a GUI.** Doing this with code only involves a lot of making small changes to numbers and then restarting the application to see what it looks like now. This is a tedious process. And if your code has to re-compile each time it's changed, that slows the process down even further. Having a visual editor for this type of thing allows you to adjust stuff based on what it looks like, and have _immediate_ feedback, which you can then use to make further adjustments.

This applies to all visual things in general. If you're working on a [particle effect](https://en.wikipedia.org/wiki/Particle_system), you're making a lot of small changes and seeing how that affects its look. Or lighting in a scene, or colors for a sprite, etc. And since a game is largely made up of its visuals, being able to adust and iterate on these things can make a big difference.

### Unity supports all the platforms I care about

I'm pretty sure the name "Unity" comes from the idea that you can write your code once and export it to any platform. While I don't think that's _entirely_ true -- there are significant differences between the platforms that you do need to take into account -- it does make the process easier.

I got a taste of the difficulty of exporting to different platforms when I was fiddling with my own C++ game engine a while ago. I only wanted to support Windows, Mac, and web (via [Emscripten](https://emscripten.org)), which is a far cry from the number of platforms supported by Unity:

// <img src="/img/unity_supported_platforms.png" style="width: 50%" />

See, the challenge isn't just in getting the code to _compile_ for the platform you're targeting, although that is definitely an issue. One big issue is that there are a lot of different APIs you have to use depending on the device you're targeting.

// <div class="sidenote">

For instance, for graphics you might think, "OpenGL is supported everywhere, why not just use that?" and you'd be partially right, because it's not quite OpenGL everywhere. It's OpenGL on desktop platforms, WebGL on the web, and OpenGL ES on mobile platforms, each a slightly different flavor of the API. And if I wanted to export to Xbox, PS4/5, or Switch, it'd be a totally different, proprietary API. It's the same story for sound and input -- no matter how cross-platform you may think the library is that you're using, there's going to be significant differences getting it to run exactly how you want when you move to a new platform.

Another issue is that file system access is not entirely the same. This is mainly an issue between desktop and web, since a program running in your browser doesn't have any filesystem to access to actually load your files from. But even then, there are lots of annoying things to worry about in C++. Do I use forward slashes or backslashes for file paths? How do I know where to go to find the asset files for the game? Why does everything in the Windows API use `WCHAR` instead of a regular `char`? In Unity this is auto-magically solved because all your files are bundled and loaded for you by the engine.

// </div>

I'm not even going to go into the difficulties of trying to build and debug a C++ app on iOS and Android. I haven't done it yet, but I'm pretty intimidated by it. I would much rather deal with Unity's quirks than try to demystify the arcane secrets of the Android NDK.

I'm not saying it's not _possible_ to work out all those things. But so far, my goal has been to finish these games, and Unity allows me to do that without having to make my own engine.

All you have to do (more or less) is click "Build" and it builds for the target of your choice. They also offer Unity Cloud Build for $9/month which is nice for pumping out the builds without having to take up time doing it on your computer. It still has some problems, like if you're having an iOS-specific issue, the debug cycle is a pain because you have to make a new build every time you make a change. But overall, Unity works *well enough* on all the platforms that I care about that it's worth it to me.

### I like C\#

C# is nice. I enjoy coding in it.

It has a progressive feature set, including stuff like:

- [the `var` keyword](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/var),
- [LINQ](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/concepts/linq/) for structured querying of collections,
- [coroutines](https://en.wikipedia.org/wiki/Coroutine) via [the yield statement](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/yield),
- and even [async/await](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/concepts/async/) if you want to get fancy.

It also has [stack-allocated structs](http://clarkkromenaker.com/post/csharp-structs/) so you can avoid a fair amount of garbage-collection. That's critical for real-time games, and it's a feature that Java, Lua, Haxe, Javascript, and most other languages don't have.

### It has a HUGE community

I can't find it now, but I saw a tweet a while back that said something like:

> Unity sucks, but the community is big enough that no matter what problem you're having, you can google it and you'll find 6 different ways to solve it.

I'm _pretty_ sure Unity is the most popular game engine out there. It definitely seems so when you're googling stuff. It may not be the best, or the fastest, and it has its fair share of bugs and crashes and broken or unfinished features. But it doesn't matter because no matter what you want to do, there's a huge amount of content online telling you how to do it. That's something that can't necessarily be said about the other engines & frameworks I've used.

## TL;DR

It's fine, I know how to use it, and I know how to find help when I'm stuck. That's pretty much all this boils down to.

I do still want to fiddle with other engines -- I just got accepted into the Luxe closed beta! -- and hope to make more progress on my own custom game engine at some point. But these are the reasons I've stuck with Unity so far.
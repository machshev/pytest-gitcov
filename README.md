# pytest-gitcov
Extension for pytest to report on the coverage for the lines modified in a given
commit or commit range. The vision is to be able to run pytests on a code base
before submitting a pull request or code review, to see the lines of code that
were modified by you but not covered by unit-tests.

## Issues this plugin is trying to resolve
- Ideally the whole code base will have reasonable coverage. Realistically
though this is rarely the case with a legacy code base. The repository wide
coverage report means little in terms of one developers merge request. The hope
is that using this plugin you can shine a light on the code you have touched.
Making it easier to spot gaps in unit tests due to code you have written, or
modified and identify a gap someone else left and should really be filled.
- Just reporting a list of line ranges covered on the terminal is not much help.
I can't remember the line numbers for the functions I've just changed, and
working out where the gaps are is time consuming. The HTML report is a lot
better for this, but I'd like to have something quick and simple for the
terminal.

## UPDATE
Since starting this project a few years ago I've changed my opinion
significantly on unit testing and TDD. At the time I'd recently started working
in a new team that had heavily bought into the mockist style of TDD as opposed
to the classicist style... also known as London and Detroit styles respectively.

If your not familiar with the difference then I'd recommend reading Martin
Fowler's excellent article (Mocks aren't
Stubs)[https://martinfowler.com/articles/mocksArentStubs.html]. Especially his
conclusions in the section "So should I be a classicist or a mockist?". Martin
leans towards classicist, however given my experience working on a large
codebase using the mockist approach I'd go further and strongly recommend
classicist style. For details see the article, but in summary...
(at least it started as a summary).

## Classicist TDD

Classicists, those who follow Kent Beck's book "Test-Driven Development". Use
black box testing, given a function/method is called with a given set of
arguments then the result or resulting state is as expected. This allows the
test to test the expected behaviours regardless of the implementation. It means
the implementation can be refactored without modifying the test. In this
approach the function and any other functions it calls are also called during
the test... including external systems and any system side effects.

Mockists's suggest test isolation can be an issue. Given a single test may
trigger many other function calls or side effects, then it might be more
difficult to find where a bug is introduced. However in my experience, if you
are using good git practices, small regular commits then it's generally obvious
what changed to break your tests. You also get faster feedback, given any
changes to the behaviour will break the test... be that in your function or a
function you are relying on to meet it's contract. Ironically, the mockest
approach allows you to commit code that assumes, but doesn't test, a dependent
functions behavioural contract. If that dependent function isn't tested, or
tested adequatly, then your test can pass and you end up committing a number of
changes before noticing the issue. It's far more difficult to then find the
issue if you have a number of changes to sift through (`git bisect` is your
friend there).

It's important to have good testing practice from the beginning of a project.
If the code is not designed to be tested then simple tests can quickly become
slow "end-to-end" tests. However the solution is fairly simple, write good
modular low coupled code. Seporating out pure functions from actions where
possible (see "grokking Simplicity"). Depend on abstractions rather than
concreations, which allows stubs to be used to fulfill the behaviours depended
on for testing purposes. Use dependency injection to make it easy to introduce
stubs. External systems can be stubed using the port adaptor style architecture.

A common complaint is test speed with this approach. However I have developed a
large library with close to 1000 unit tests using the strategy outligned above.
The whole test suit taking about 30 seconds to run - which is fine for a
pre-commit check. Most test runners allow you to run a cut down set of tests for
just the dir/module/file your developing, or rerun the last failed tests. This
makes iterating fast using red/green/refactor TDD really fast, and then when
ready to commit you can run the full suit to double check you havent broken
anything else.

Basically with good software development practices Classicist TDD is not an
issue, on the contrary it supports fast and robust development..

## Mockists TDD

Mockists on the other hand uses mocks in place of all dependencies, both
internal and external. Testing a function performs an expected set of
interactions. This means you can write really high level tests from the
beginning, starting right from the top and then implement everything downwards
in layers. The classicist can do something similar with stubs and dependency
injection.

There are several issues with this:

- Tests are testing the implementation and not the effect or outcome of the
function/method. If you need to change the implementation as part of a
refactoring effort, then you essentially need to throw away the test and rewrite
it. But this effect also cascades, it effects every test that uses your function
as a mock if the interface changes. Whereas the classicist only needs to change
the tests that test the function who's interface has changed (as well as the
code using that function in the main code base).

- You can't really do TDD properly with mockest approach. With TDD you write a
red test, a failing test, but nevertheless a test that is supposed to correctly
check the function behaves as expected. Then having seen the test fail without
the function implemented, add the code to make the test go green. This guards
against writing tests that pass without checking anything... forgetting to
assert, or there is a bug in the test logic. With the mockest approach, your
testing the code flow within the function and mocking external function calls.
However you can't really do that without first working out how you are going to
implement the functionality first. So you end up with a strange back and forth
where the code is written alongside the unittest. This is whitebox testing,
because you need to know the function implementation before you can complete the
test. But then what is the red stage?

- While the tests isolate the behaviours of a function well, they assume the
dependencies are implemented correctly and that other tests assert that. However
this is not always the case. I've seen many examples where mockist unit tests
pass when the dependant functions are broken, and therefore the behaviour of the
function under test is also broken.

- Only works if the test coverage is very high. Because there is such a reliance
that all mocked objects are tested elsewhere independently, the testing burden
is really high. Whereas the classicist might implicitly test a set of behaviours
together, the mockest has to test everything independently. This often leads to
poor quality tests due to demotivation, exacibating the issue. Writing tests
designed to maximise coverage stats and not neseserily code quality.

In the end we ended up with a legacy big ball of mud. Any code change resulted
in 10x time to fix up the existing tests to get those to pass as well as any new
ones you added to cover new functionality. The software team ground to a virtual
halt... but through the magic powers of scrum velocity points relative to
nothing but themselves, the team was still "performing". To compensate, features
were broken down into smaller chunks and estimates inflated to match the new
norm. Moving back to a classicist approach was such a relief, so much easier to
write meaningful tests, and development speed really took off.

## Development

I'm mixed about this project now. Currently I don't have any use for the
functionality, which is why development has been put on hold for the moment.
Maybe someday I'll have a need again and continue development on this.

# Install

Nice and easy: `pip install pytest-gitcov`

# Usage

This is still in very early stages of development and doesn't really do much
yet.

After installing, the plugin is automatically found by pytest. At the moment
that means that the plugin always runs with each `pytest` run and you have to
uninstall to disable it. Soon there should be an extra argument that can be used
to temporarily disable this. For example, respect the existing `pytest-cov` flag
(`--no-cov`) as well as a new `--no-gitcov` flag .

There is also a standalone script available to generate a git coverage report on
previous `.coverage` DB file, for more info see `git-py-coverage --help`.

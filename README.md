# systems-mechanism-lab

A reusable laboratory for learning how computer systems actually work.

The repository is not organized as a collection of ordinary reading notes. Its purpose is to turn system knowledge into **mechanisms that can be explained, observed, tested, falsified, and transferred**.

It is intentionally general enough to host learning tracks for Unix/Linux, Kafka, MySQL, Redis, JVM, networking, storage, and other systems.

## Core idea

> Chapters provide navigation. Mechanisms provide structure. Experiments provide evidence.

The default learning loop is:

**Question → Hypothesis → Source model → Experiment → Observation → Evidence → Conclusion → Boundary → Transfer**

A topic is not considered learned merely because its documentation or source text has been read. Important claims should be made observable whenever practical.

## Repository structure

```text
docs/
  LEARNING_MECHANISM.md      # repository-wide learning protocol
templates/
  MECHANISM_UNIT.md          # template for one mechanism
  EXPERIMENT.md              # template for a reproducible experiment
topics/
  <system>/                  # unix, kafka, mysql, redis, ...
```

Individual systems may follow books or documentation chapter-by-chapter for coverage, but durable knowledge should ultimately be organized around mechanisms rather than book structure.

## Start here

Read [`docs/LEARNING_MECHANISM.md`](docs/LEARNING_MECHANISM.md) before adding a new learning track.

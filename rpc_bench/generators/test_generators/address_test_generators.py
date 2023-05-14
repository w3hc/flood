from __future__ import annotations

import typing

import rpc_bench


def generate_test_eth_get_balance(
    rates: typing.Sequence[int],
    duration: int,
    vegeta_kwargs: typing.Mapping[str, str | None] | None = None,
    random_seed: rpc_bench.RandomSeed | None = None,
) -> rpc_bench.LoadTest:
    n_calls = rpc_bench.estimate_call_count(rates=rates, duration=duration)
    calls = rpc_bench.generate_calls_eth_get_eth_balance(n_calls=n_calls)
    return rpc_bench.construct_load_test(
        calls=calls,
        rates=rates,
        duration=duration,
    )


def generate_test_eth_get_transaction_count(
    rates: typing.Sequence[int],
    duration: int,
    vegeta_kwargs: typing.Mapping[str, str | None] | None = None,
    random_seed: rpc_bench.RandomSeed | None = None,
) -> rpc_bench.LoadTest:
    n_calls = rpc_bench.estimate_call_count(rates=rates, duration=duration)
    calls = rpc_bench.generate_calls_eth_get_transaction_count(n_calls=n_calls)
    return rpc_bench.construct_load_test(
        calls=calls,
        rates=rates,
        duration=duration,
    )


####################################################################
####################################################################
####################################################################

# This is hacky but convenient to define variables.
# Source: https://stackoverflow.com/a/41586688

import inspect
import dis

def get_assigned_name(frame):
    """Takes a frame and returns a description of the name(s) to which the
    currently executing CALL_FUNCTION instruction's value will be assigned.

    fn()                    => None
    a = fn()                => "a"
    a, b = fn()             => ("a", "b")
    a.a2.a3, b, c* = fn()   => ("a.a2.a3", "b", Ellipsis)

    Usage: get_assigned_name(inspect.currentframe().f_back)
    """

    iterator = iter(dis.get_instructions(frame.f_code))
    for instr in iterator:
        if instr.offset == frame.f_lasti:
            break
    else:
        assert False, "bytecode instruction missing"
    assert instr.opname.startswith('CALL_')
    try:
        instr = next(iterator)
    except StopIteration:
        raise Exception("missing bytecode instruction") from None
    if instr.opname == 'POP_TOP':
        raise ValueError("not assigned to variable")
    if instr.opname != 'STORE_NAME':
        raise ValueError("unsupported code to identify variable name")
    return instr.argval

####################################################################
####################################################################
####################################################################

import sympy as sy

def def_scalar_param(name=None, **kwargs) -> sy.Symbol:
    """Define a sympy scalar parameter.

    By default assume `nonnegative=True`.
    """
    if name is None:
        name = get_assigned_name(inspect.currentframe().f_back)
    if "nonnegative" not in kwargs:
        kwargs["nonnegative"] = True
    return sy.Symbol(name, **kwargs)


def def_vector_param(name=None, **kwargs) -> sy.IndexedBase:
    """Define a sympy vector parameter.

    By default assume `nonnegative=True`.
    """
    if name is None:
        name = get_assigned_name(inspect.currentframe().f_back)
    if "nonnegative" not in kwargs:
        kwargs["nonnegative"] = True
    return sy.IndexedBase(name, **kwargs)

####################################################################
####################################################################
####################################################################

def pull_production_with_capacity_limit(model, object_id, limit_object, limit_processes, capacity, **kwargs):
    """Helper to set up 'pull production' with a capacity limit"""

    # Initial proposal for required production, before considering the capacity limit
    proposal = model.pull_production(
        object_id,
        model.object_production_deficit(object_id),
        **kwargs
    )

    # Limit by capacity
    limited = model.limit(
        proposal,
        model.expr("SoldProduction", object_id=limit_object, limit_to_processes=limit_processes),
        capacity,
    )

    return limited

####################################################################
####################################################################
####################################################################

from attrs import evolve

def update_sankey_data(sankey_data, new_flow_values):
    """Replace link values with new values.

    Each link in `sankey_data` has its "value" data set to the sum of the values
    in `new_flow_values` corresponding to the link's original flow ids.

    TODO: add to floweaver, generalise aggregation function.
    """
    new_links = [
        evolve(link, data={
            **link.data,
            "value": sum(
                new_flow_values[k]
                for k in link.original_flows
                if new_flow_values[k] > 1e-6
            )
        })
        for link in sankey_data.links
    ]
    new_sankey_data = evolve(sankey_data, links=new_links)
    return new_sankey_data
